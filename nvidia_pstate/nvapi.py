import ctypes
import sys
import platform

# Library
_lib = None

# Load library
if sys.platform.startswith("linux"):
  _lib = ctypes.CDLL("libnvidia-api.so")
elif sys.platform.startswith("win32"):
  if platform.architecture()[0].startswith("64bit"):
    _lib = ctypes.CDLL("nvapi64.dll")
  else:
    _lib = ctypes.CDLL("nvapi.dll")

if not _lib:
  raise AssertionError(f"Unsupported operating system: {sys.platform}")

# (undocumented)
_nvapi_QueryInterface = _lib.nvapi_QueryInterface
_nvapi_QueryInterface.argtypes = [ctypes.c_int]
_nvapi_QueryInterface.restype = ctypes.c_void_p
def nvapi_QueryInterface(address: int) -> ctypes.c_void_p:
  return _nvapi_QueryInterface(address)

# https://docs.nvidia.com/gameworks/content/gameworkslibrary/coresdk/nvapi/group__nvapifunctions.html#ga773e227cecd41f303965a89446baa5e3
_NvAPI_Initialize_ptr   = nvapi_QueryInterface(0x0150e828)
_NvAPI_Initialize_proto = ctypes.CFUNCTYPE(ctypes.c_int)
_NvAPI_Initialize       = ctypes.cast(_NvAPI_Initialize_ptr, _NvAPI_Initialize_proto)
def NvAPI_Initialize() -> int:
  """
    This function initializes the NvAPI library (if not already initialized) but always increments the ref-counter. This must be called before calling other NvAPI_ functions. Note: It is now mandatory to call NvAPI_Initialize before calling any other NvAPI. NvAPI_Unload should be called to unload the NVAPI Library.
  """

  return _NvAPI_Initialize()

# https://docs.nvidia.com/gameworks/content/gameworkslibrary/coresdk/nvapi/group__nvapifunctions.html#gaac13a47b132d2aa6e2ca01731f9244e3
_NvAPI_Unload_ptr   = nvapi_QueryInterface(0xd22bdd7e)
_NvAPI_Unload_proto = ctypes.CFUNCTYPE(ctypes.c_int)
_NvAPI_Unload       = ctypes.cast(_NvAPI_Unload_ptr, _NvAPI_Unload_proto)
def NvAPI_Unload() -> int:
  """
    Decrements the ref-counter and when it reaches ZERO, unloads NVAPI library. This must be called in pairs with NvAPI_Initialize.
  """

  return _NvAPI_Unload()

# https://docs.nvidia.com/gameworks/content/gameworkslibrary/coresdk/nvapi/group__gpu.html#gaf838839f5aca4bd6cdb60fc743ae8ef4
_NvAPI_EnumPhysicalGPUs_ptr   = nvapi_QueryInterface(0xe5ac921f)
_NvAPI_EnumPhysicalGPUs_proto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
_NvAPI_EnumPhysicalGPUs       = ctypes.cast(_NvAPI_EnumPhysicalGPUs_ptr, _NvAPI_EnumPhysicalGPUs_proto)
def NvAPI_EnumPhysicalGPUs(nvGPUHandle: ctypes.c_void_p, pGpuCount: ctypes.c_void_p) -> int:
  """
    This function returns an array of logical GPU handles.

    Each handle represents one or more GPUs acting in concert as a single graphics device.

    At least one GPU must be present in the system and running an NVIDIA display driver.

    The array nvGPUHandle will be filled with logical GPU handle values. The returned gpuCount determines how many entries in the array are valid.
  """

  return _NvAPI_EnumPhysicalGPUs(nvGPUHandle, pGpuCount)

# https://docs.nvidia.com/gameworks/content/gameworkslibrary/coresdk/nvapi/group__gpupstate.html#gaeffe0838ca9850b9984fa9be117f637e
_NvAPI_GPU_GetPstates20_ptr   = nvapi_QueryInterface(0x6ff81213)
_NvAPI_GPU_GetPstates20_proto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
_NvAPI_GPU_GetPstates20       = ctypes.cast(_NvAPI_GPU_GetPstates20_ptr, _NvAPI_GPU_GetPstates20_proto)
def NvAPI_GPU_GetPstates20(hPhysicalGpu: ctypes.c_void_p, pPstatesInfo: ctypes.c_void_p) -> int:
  """
    P-States are GPU active/executing performance capability states.
    They range from P0 to P15, with P0 being the highest performance state,
    and P15 being the lowest performance state. Each P-State, if available,
    maps to a performance level. Not all P-States are available on a given system.
    The definition of each P-States are currently as follow:
    - P0/P1 - Maximum 3D performance
    - P2/P3 - Balanced 3D performance-power
    - P8 - Basic HD video playback
    - P10 - DVD playback
    - P12 - Minimum idle power consumption
  """

  return _NvAPI_GPU_GetPstates20(hPhysicalGpu, pPstatesInfo)

# (undocumented)
_NvAPI_GPU_SetForcePstate_ptr   = nvapi_QueryInterface(0x025bfb10)
_NvAPI_GPU_SetForcePstate_proto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)
_NvAPI_GPU_SetForcePstate       = ctypes.cast(_NvAPI_GPU_SetForcePstate_ptr, _NvAPI_GPU_SetForcePstate_proto)
def NvAPI_GPU_SetForcePstate(hPhysicalGpu: ctypes.c_void_p, pstate: int, int3: int) -> int:
  return _NvAPI_GPU_SetForcePstate(hPhysicalGpu, pstate, int3)
