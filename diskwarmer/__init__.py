from docopt import docopt
from vmtouchparser import parse

usage = \
"""
diskwarmer. Heats up files into the disk cache from previously
      produced vmtouch -v report.

Usage:
  warm [options] sort <report>

Options:
  -h --help        Show this screen.
  --version        Show version.
"""

def do_sort(path):
    records = parse(path)
    density = [(float(x.resident)/x.size, x.name) for x in records]
    for (x, name) in sorted(density, reverse=True):
        print x, name

def main():
    args = docopt(usage)
    if args['sort']:
        return do_sort(args['<report>'])

if __name__ == "__main__":
    main()

