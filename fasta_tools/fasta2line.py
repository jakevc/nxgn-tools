#!/usr/bin/env python3.6
import argparse


def get_arguments():
    '''Define and return command line options.'''
    parser = argparse.ArgumentParser(prog='fasta2line',
                                     description='This program \
                                     converts a multiline \
                                     to a two-line fasta')

    parser.add_argument('-i', '--infile',
                        help='specify input file (path)',
                        required=True,
                        type=argparse.FileType('rt',
                                               encoding='UTF-8 '))
    parser.add_argument('-o', '--outfile',
                        help='specify output file (path)',
                        required=False,
                        type=argparse.FileType('wt',
                                               encoding='UTF-8 '))
    return parser.parse_args()


# return command line arguments for use
args = get_arguments()

# get input file
infile = args.infile.name

# get output file
outfile = args.infile.name+'_2li'

# firstline case
firstline = True
# open files for reading and writing
with open(infile, 'r') as i, open(outfile, 'w') as o:
    # loop over the file
    NR = 0
    for line in i:
        # for only the firstline
        if firstline and line.startswith('>'):
            o.write(line)
            firstline = False
            NR += 1
        # elif header lines
        elif line.startswith('>'):
            o.write('\n'+line)
            NR += 1
        # write sequence lines
        else:
            if line.startswith('>') is False and line != '':
                line = line.strip()
                o.write(line)
            NR += 1
            if NR % 1000 == 0:
                print(f'Processed line: {NR}')
    print('Done')
