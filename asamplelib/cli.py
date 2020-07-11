"""Console script for asamplelib"""
import argparse
import sys

import asamplelib


def main():
    """Console script for asamplelib."""
    parser = argparse.ArgumentParser()
    parser.add_argument("_", nargs="*")
    args = parser.parse_args()

    print("Arguments: " + str(args._))

    asamplelib.sayHello()
    print("3 + 5 = " + str(asamplelib.sum(3, 5)))

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
