#!/usr/bin/env python

import argparse
import datetime
import fileinput
import sys


def _parse_args():
    last_month_date = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
    parser = argparse.ArgumentParser(description="Parse Mint export data and look for transactions with the tag 'shared'")
    parser.add_argument('--month',
                        type=str,
                        default=str(last_month_date.month),
                        help="Month to parse (Jan = 1, Feb = 2, etc.)")
    parser.add_argument('--year',
                        type=str,
                        default=str(last_month_date.year),
                        help="Year to parse (YYYY)")
    parser.add_argument('--tag',
                        type=str,
                        default='shared',
                        help="Tag to filter by")
    parser.add_argument('filename',
                        help="The csv file to parse")

    return parser.parse_args()


def main():
    args = _parse_args()
    for line in fileinput.input([args.filename]):
        if not fileinput.isfirstline():
            values = line.split(',', 8)
            # date is MM/DD/YY
            if len(values) >= 9:
                date = values[0].strip('"')
                vendor = values[1].strip('"')
                cost = values[3].strip('"')
                cat = values[5].strip('"')
                tag = values[7].strip('"')
                notes = values[8].strip('"').strip('\n')
                try:
                    if args.month == date.split('/')[0] and args.year in date.split('/')[2]:
                        if args.tag in tag.lower():
                            sys.stdout.write('%s\n' % ','.join([date, vendor, cost, cat, tag, notes]))
                except ValueError:
                    print "Could not parse date: %s" % date

if __name__ == '__main__':
    main()
