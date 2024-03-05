import atexit
import ctypes
import os
import sys

from .nvapi import NvAPI_Initialize, NvAPI_Unload, NvAPI_EnumPhysicalGPUs, NvAPI_GPU_SetForcePstate


# Initialize NvAPI
if NvAPI_Initialize() != 0:
  print("Failed to initialize NvAPI", file=sys.stderr)

def NvAPI_Unload_atexit():
  # Unload NvAPI
  if NvAPI_Unload() != 0:
    print("Failed to unload NvAPI")
    return

# Unload NvAPI at exit
atexit.register(NvAPI_Unload_atexit)


def set_pstate(ids, pstate, *, silent = False):
  # Default ids: all or limited by CUDA_VISIBLE_DEVICES
  if ids is None:
    ids = []

  # Default pstate: let driver decide
  if pstate is None:
    pstate = 16

  # Array to hold GPU handles
  gpu_array = (ctypes.c_void_p * 64)()

  # Integer to hold GPU count
  gpu_count = ctypes.pointer(ctypes.c_int32())

  # Enumerate GPUs
  if NvAPI_EnumPhysicalGPUs(gpu_array, gpu_count) != 0:
    print("Failed to enumerate GPUs", file=sys.stderr)
    return

  # GPU count as int
  gpu_count = gpu_count.contents.value

  # Function to actually set performance state
  def _set_performance_state(gpu_id, pstate):
    if not (0 <= gpu_id < gpu_count):
      if not silent:
        print(f"Invalid GPU ID: {gpu_id}", file=sys.stderr)
      return

    if NvAPI_GPU_SetForcePstate(gpu_array[gpu_id], pstate, 2) == 0:
      if not silent:
        print(f"Performance state has been set successfully for gpu #{gpu_id}", file=sys.stderr)
    else:
      if not silent:
        print(f"Failed to set performance state for gpu #{gpu_id}", file=sys.stderr)

  # If GPUs is not specified, try to use CUDA_VISIBLE_DEVICES
  if len(ids) == 0:
    visible_devices = os.getenv("CUDA_VISIBLE_DEVICES")
    if visible_devices:
      for device in visible_devices.split(","):
        ids.append(int(device))

  # Set performance state for specified GPU or all GPUs
  if len(ids) == 0:
    for i in range(gpu_count):
      _set_performance_state(i, pstate)
  else:
    for i in ids:
      _set_performance_state(i, pstate)

def set_pstate_low():
  set_pstate([], int(os.getenv("NVIDIA_PSTATE_LOW", "8")), silent=True)

def set_pstate_high():
  set_pstate([], int(os.getenv("NVIDIA_PSTATE_HIGH", "16")), silent=True)
