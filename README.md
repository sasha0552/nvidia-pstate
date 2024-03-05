# nvidia-pstate
A library and CLI utilities for managing performance states of NVIDIA GPUs.

## Installation
```sh
pip3 install nvidia_pstate
```

## Usage (CLI)
```sh
# List available performance states (TODO: does not work right now, use nvidia-smi -q and count memory clocks)
nvidia-pstate list-pstates

# Set performance state for specific GPU
nvidia-pstate set-pstate -i 0 -ps 0

# Let driver decide which performance state GPU should use
nvidia-pstate set-pstate -i 0 -ps 16

# Set performance state for all GPUs
nvidia-pstate set-pstate -ps 0
```

## Usage (API)
```python
from nvidia_pstate import set_pstate_low, set_pstate_high

set_pstate_low() # set pstate to "low" level (8 by default)
set_pstate_high() # set pstate to "high" level (16 by default)

# default values can be overrided using NVIDIA_PSTATE_LOW and NVIDIA_PSTATE_HIGH environment variables.
```
