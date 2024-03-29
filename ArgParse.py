#https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df
import argparse
parser = argparse.ArgumentParser(description='Add some integers.')

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='interger list')

parser.add_argument('--sum', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()

print(args.sum(args.integers))