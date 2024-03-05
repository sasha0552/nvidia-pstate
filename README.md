# nvidia-pstate
A library and CLI utilities for managing performance states of NVIDIA GPUs.

## Installation
```sh
pip3 install nvidia_pstate
```

## Usage
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
