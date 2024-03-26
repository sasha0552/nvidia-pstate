import argparse
import importlib.metadata

import nvidia_pstate


# Function to list available performance states
def query_pstate(args):
  # TODO
  print("Does not work for now")

# Function to specify performance state
def set_pstate(args):
  nvidia_pstate.set_pstate(args.id, args.perf_state, silent=args.silent)


def main():
  # Determine program version
  try:
    __version__ = importlib.metadata.version("nvidia-pstate")
  except:
    __version__ = "unknown"

  # Create the main argument parser with a description
  parser = argparse.ArgumentParser(description="CLI utility for managing performance states of NVIDIA GPUs")

  parser.add_argument("-i", "--id", type=int, nargs="+", help="target a specific GPU")
  parser.add_argument("-ps", "--perf-state", type=int, help="specify performance state")
  parser.add_argument("-q", "--query", action="store_true", help="list available performance states")
  parser.add_argument("-s", "--silent", action="store_true", help="suppress output messages")
  parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")

  # Parse command-line arguments
  args = parser.parse_args()

  # Execute the appropriate function
  if args.perf_state is not None:
    set_pstate(args)
  elif args.query is not None and args.query:
    query_pstate(args)
  else:
    parser.print_help()
