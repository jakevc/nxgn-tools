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

# open files for reading and writing
with open(infile, 'r') as i, open(outfile, 'w') as o:
    # loop over the file
    for line in i:
        # for only the firstline
        firstline = True
        if firstline and line.startswith('>'):
            o.write('\n'+line)
            firstline = False
        # if write header lines
        elif line.startswith('>'):
            o.write(line+'\n')
        # write sequence lines
        else:
            if line.startswith('>') is False and line != '':
                line = line.strip()
                o.write(line)
