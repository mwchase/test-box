import argparse

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers()

prep = subparsers.add_parser('prep')

test = subparsers.add_parser('test')

report = subparsers.add_parser('report')

parser.parse_args()
