import argparse
import sys
from pathlib import Path

from .interior import main as main_interior
from .map import main as main_map
from .surrounding import main as main_surrounding


class ParseArguments:

    def __init__(self):
        parser = argparse.ArgumentParser(description='')
        parser.add_argument('command', help='Subcommand to run')

        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)

        getattr(self, args.command)()

    def interior(self):
        parser = argparse.ArgumentParser(
            description='')
        parser.add_argument('file', type=str,
                            help='Path to file that contains list of zip codes')
        parser.add_argument('--radius', type=int, default=0,
                            help='Search radius for surrounding zip codes')
        parser.add_argument('--map', action="store_true",
                            help="Provide URL to view zip code boundaries in a map")
        parser.add_argument('--title', type=str, default="Zip Codes",
                            help='Title for map of zip code boundaries')

        args = parser.parse_args(sys.argv[2:])

        exit(main_interior(Path(args.file).read_text(),
                           args.radius, args.map, args.title))

    def surrounding(self):
        parser = argparse.ArgumentParser(
            description='')
        parser.add_argument('file', type=str,
                            help='Path to file that contains list of zip codes')
        parser.add_argument('--radius', type=int, default=0,
                            help='Search radius for surrounding zip codes')
        parser.add_argument('--map', action="store_true",
                            help="Provide URL to view zip code boundaries in a map")
        parser.add_argument('--title', type=str, default="Zip Codes",
                            help='Title for map of zip code boundaries')

        args = parser.parse_args(sys.argv[2:])

        exit(main_surrounding(Path(args.file).read_text(),
                              args.radius, args.map, args.title))

    def map(self):
        parser = argparse.ArgumentParser(
            description='Provide URL to view zip code boundaries in a map')
        parser.add_argument('file', type=str,
                            help='Path to file that contains list of zip codes')
        parser.add_argument('--title', type=str, default="Zip Codes",
                            help='Title for map of zip code boundaries')

        args = parser.parse_args(sys.argv[2:])

        exit(main_map(Path(args.file).read_text(), args.title))


def main() -> int:
    ParseArguments()

    return 0


if __name__ == '__main__':
    exit(main())
