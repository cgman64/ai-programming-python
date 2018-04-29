# Introducing Optional arguments

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
					action="store_true") # The action param now makes the option more of a flag than something that requires a value.
args = parser.parse_args()
if args.verbose:
	print("verbosity turned on")