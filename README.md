# Spearmint

Extract transactions from exported mint.com data for a given month and year with a
given tag.

## Examples

    $ ./spearmint.py --month 1 --year 2014 /path/to/mint.csv > 1-2014.csv

Extract transactions for January 2014.

    $ ./spearmint.py /path/to/mint.csv > lastmonth.csv

Extract transactions from the previous month.
