#!/usr/bin/env python3.6

"""
length_dist.py computes the read length distribution of a fasta file
"""

import argparse
import collections


def get_args():
    '''Define and return command line options.'''
    parser = argparse.ArgumentParser(prog='length_dist',
                                     description='Calculates the length\
                                     distribution of a fasta file.')
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


def sort_dec(unsorted_dict):
    '''Sort the values of a dictionary on decending values.'''
    return dict(sorted(unsorted_dict.items(), key=(lambda x: (x[0])),
                reverse=True))


def length_freq(infile):
    # loop through file, soring counts of read length
    with open(infile, 'r') as ifi:
        for line in ifi:
            if not line.startswith('>'):
                cnt[len(line)] += 1
            else:
                None


def write_out(outfile):
    cnt_sort = sort_dec(cnt)
    # write read length frequency to outfile
    with open(outfile, 'w') as ofi:
        ofi.write('Length\tCounts\n')
        for k, cnt_sort[k] in cnt_sort.items():
            ofi.write(f'{k}\t{cnt[k]}\n')


# return parsed arguments
args = get_args()

# cash the infile
infile = args.infile.name

# ... outfile
outfile = args.outfile.name

# initialize empty dict to store counts
cnt = collections.Counter()

# call length freq on infile
length_freq(infile)

# write out distribution
write_out(outfile)
