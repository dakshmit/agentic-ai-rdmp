import argparse
parser = argparse.ArgumentParser(description = "Simple CLI test")
parser.add_argument("--name", type=str, required = True , help="Your name")
parser.add_argument("--age", type=int, required=True, help="Your age")
args= parser.parse_args()
print(f"Hello {args.name}, you are {args.age} years old.")