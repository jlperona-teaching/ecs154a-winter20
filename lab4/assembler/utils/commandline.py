import argparse

# command line argument parsing
def argument_parsing():
    parser = argparse.ArgumentParser(
        description = 'Take in a CSV file with Lab 4 assembly code. '
            'Output a text file to load into a RAM in Logisim Evolution. '
            'All values, including immediate values, must be in decimal. '
            'Immediate values can be negative.'
    )

    # mandatory input file
    parser.add_argument('infile',
        metavar = 'input.csv',
        help = 'Input CSV file with valid assembly code.'
    )

    # optional output file
    parser.add_argument('outfile',
        nargs = '?',
        help = 'If specified, write to an output file instead of the console. '
            'Output file will be overwritten.'
    )

    # no header flag
    parser.add_argument('-n',
        '--noheader',
        action = 'store_true',
        help = 'Treat the first row of the file as a line of code. '
            'Normal behavior treats the first line as a header and skips it.'
    )

    # binary flag
    parser.add_argument('-b',
        '--binary',
        action = 'store_true',
        help = 'Export binary instead of hexadecimal.'
    )

    return parser.parse_args()
