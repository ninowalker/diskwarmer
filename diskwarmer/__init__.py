from pyparsing import nums as digits
from pyparsing import alphas, LineStart, LineEnd, Word, Literal, Regex, ZeroOrMore, OnlyOnce

whole_number = Word(digits)
whole_number_ratio = whole_number + Literal("/") + whole_number

rational_number = Regex("[0-9]+\.[0-9]+")

unit = Regex("[BKMGT]")
unit_ratio = whole_number + unit + Literal("/") + whole_number + unit

file_name = Regex("[^\n\r]+") #TODO IMPROVE THIS

mapped = Regex("[Oo ]*")
mapped_pic = Literal("[") + mapped + Literal("]")

fileline = file_name + LineEnd()
mapline = mapped_pic + whole_number_ratio + LineEnd()
record = fileline + mapline

files_stat     = Literal("Files:") + whole_number + LineEnd()
dirs_stat      = Literal("Directories:") + whole_number + LineEnd()
resident_stat  = Literal("Resident Pages:") + whole_number_ratio + unit_ratio + rational_number + Literal("%") + LineEnd()
elapsed_stat   = Literal("Elapsed:") + rational_number + Literal("seconds") + LineEnd()
all_stats      = files_stat + dirs_stat + resident_stat + elapsed_stat

vmtouch_parser = ZeroOrMore(record) + all_stats

def parse(file):
    records = []
    def parseRecord(str, loc, toks):
      record = {}
      record['name'] = toks[0]
      record['pic'] = toks[3]
      record['resident'] = int(toks[5])
      record['size'] = int(toks[7])
      records.append(record)
    record.setParseAction( parseRecord )
    vmtouch_parser.parseFile(file)
    return records

from docopt import docopt
usage = \
"""
warm. Heats up files into the disk cache from previously
      produced vmtouch -v report.

Usage:
  warm [options] sort <report>

Options:
  -h --help        Show this screen.
  --version        Show version.
"""

def do_sort(path):
    records = parse(path)
    density = [ (float(x['resident'])/x['size'], x['name'] ) for x in records]
    for (x, name) in sorted(density):
        print x, name

def main():
    args = docopt(usage)
    if args['sort']:
        return do_sort(args['<report>'])

if __name__ == "__main__":
    main()

