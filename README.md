# nvidia-pstate
A library and CLI utilities for managing performance states of NVIDIA GPUs.

> [!IMPORTANT]
Try the new implementation - [nvidia-pstated](https://github.com/sasha0552/nvidia-pstated). The daemon does not require application patching and switches performance states automatically.

## Installation
### Prerequirements
#### Linux
Make sure you have the proprietary NVIDIA driver and the package providing `libnvidia-api.so` installed.

- ArchLinux: `nvidia-utils`
- Debian: `libnvidia-api1` or `libnvidia-tesla-api1` (depending on the GPU and driver installed)
- Ubuntu: `libnvidia-gl-535` (?)

On Debian derivatives, you can use `apt search libnvidia-api.so.1` to find the package you need.

#### Windows
Make sure the NVIDIA driver is installed.

### Installation
```sh
pip3 install nvidia_pstate
```

## Usage (CLI)
```sh
# List available performance states (TODO: does not work right now, use nvidia-smi -q and count memory clocks)
nvidia-pstate -q

# Set performance state for specific GPU
nvidia-pstate -i 0 -ps 0

# Let driver decide which performance state GPU should use
nvidia-pstate -i 0 -ps 16

# Set performance state for specific GPUs
nvidia-pstate -i 0 1 3 4 -ps 0

# Set performance state for all GPUs
nvidia-pstate -ps 0
```

## Usage (API)
```python
from nvidia_pstate import set_pstate_low, set_pstate_high

set_pstate_low() # set pstate to "low" level (8 by default)
set_pstate_high() # set pstate to "high" level (16 by default)

# default values can be overrided using NVIDIA_PSTATE_LOW and NVIDIA_PSTATE_HIGH environment variables.
```
