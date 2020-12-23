import argparse

parser = argparse.ArgumentParser()
parser.add_argument("x",
                    type=int,
                    help="The Base")
parser.add_argument("y",
                    type=int,
                    help="The Exponent")
parser.add_argument("-v",
                    "--verbosity",
                    action="count",
                    default=0,
                    help="Increase Output Verbosity")

args = parser.parse_args()
answer = args.x**args.y
if args.verbosity >= 2:
    print(f"{args.x} to the power {args.y} equals {answer}")
elif args.verbosity >= 1:
    print(f"{args.x}^{args.y} == {answer} ")
else:
    print(answer)
