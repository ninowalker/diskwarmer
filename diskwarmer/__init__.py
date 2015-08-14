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

def sort_by_mapped_ratio(records):
  return sorted(records, key=lambda x: x.ratio, reverse=True)

def do_sort(path):
    records = parse(path)
    total_resident = reduce(lambda t,x: t+x.resident, records, 0)
    total_size = reduce(lambda t,x: t+x.size, records, 0)
    sum_resident = 0
    sum_size = 0
    for x in sort_by_mapped_ratio(records):
        sum_resident += x.resident
        sum_size += x.size
        print '['+x.pic+']', sum_resident, sum_size, x.name

def main():
    args = docopt(usage)
    if args['sort']:
        return do_sort(args['<report>'])

if __name__ == "__main__":
    main()

