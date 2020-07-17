"""Console script for asamplelib"""
import argparse
import sys

# import asamplelib
from asamplelib import asamplelib as asa

# from asamplelib.asamplelib import sayHello, sum


def main():
    """Console script for asamplelib."""
    parser = argparse.ArgumentParser()
    parser.add_argument("_", nargs="*")
    args = parser.parse_args()

    print("Arguments: " + str(args._))

    asa.sayHello()
    print("3 + 5 = " + str(asa.sum(3, 5)))

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
