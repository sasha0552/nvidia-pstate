import atexit
import sys

# Try to use NvAPI
try:
  from .nvapi import NvAPI_Initialize, NvAPI_Unload

  # Initialize NvAPI
  if NvAPI_Initialize() != 0:
    raise Exception("Failed to initialize NvAPI")

  # Unload NvAPI at exit
  atexit.register(NvAPI_Unload)

  # Import functions
  from .pstate_nvapi import set_pstate, set_pstate_high, set_pstate_low
except Exception as e:
  # Print exception
  print(e, file=sys.stderr)

  # Define noop function
  noop = lambda *args, **kwargs: None

  # Use noop function instead of real functions
  set_pstate = noop
  set_pstate_high = noop
  set_pstate_low = noop
