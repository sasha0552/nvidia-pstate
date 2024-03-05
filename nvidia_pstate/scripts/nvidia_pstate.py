import argparse

from nvidia_pstate import set_pstate


def list_command(args):
  # TODO
  print("Does not work for now")

# Function to set performance state
def set_command(args):
  set_pstate(args.id, args.performance_state)

def main():
  # Create the main argument parser with a description
  parser = argparse.ArgumentParser(description="CLI utility for managing performance states of NVIDIA GPUs.")

  # Create subparsers for different commands
  subparsers = parser.add_subparsers(title="Commands", dest="command", required=True)

  # "list" command parser
  list_parser = subparsers.add_parser("list-pstates", help="List available performance states of GPU")
  list_parser.add_argument("-i", "--id", type=int, nargs="+", help="Target a specific GPU")
  list_parser.set_defaults(func=list_command)

  # "set" command parser
  set_parser = subparsers.add_parser("set-pstate", help="Set performance state for GPU")
  set_parser.add_argument("-i", "--id", type=int, nargs="+", help="Target a specific GPU")
  set_parser.add_argument("-ps", "--performance-state", type=int, required=True, help="Specifies performance state.")
  set_parser.set_defaults(func=set_command)

  # Parse command-line arguments and execute the appropriate function
  args = parser.parse_args()
  args.func(args)
