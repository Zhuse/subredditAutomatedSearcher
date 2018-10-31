import argparse
from definitions import begin

parser = argparse.ArgumentParser(description='Enter search params.')

parser.add_argument('-s', '--s', help='Subreddit to search.', required=True)
parser.add_argument('-p', '--p', help='Search param strings.', required=True)
parser.add_argument('-t', '--t', type=int, help='Time between each search in seconds.', required=True)

args = vars(parser.parse_args())
begin(args);




