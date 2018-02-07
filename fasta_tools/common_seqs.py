#! /usr/bin/env python3.6

'''
This script returns the 10 most frequent sequences and their counts from
a given fasta file.
'''

# move around a directory
import argparse
from collections import Counter


def get_args():
    '''Define and return command line arguments'''
    parser = argparse.ArgumentParser(
        prog='common_seqs',
        description='Determins k most common sequences with length \
        greater than 30nts from fasta file, returns seq and counts')
    parser.add_argument('fasta',
                        help='input fasta file (path)',
                        type=str)
    parser.add_argument('k',
                        type=int,
                        help='Specify the k most common seqs.\
                        Default: 10',
                        default=10,
                        nargs='?')
    return parser.parse_args()


def common_seqs(file):
    # assign empty dict
    seq_counter = Counter()

    # loop over seqs in file
    with open(file, 'r') as fh:
        NR = 1
        for line in fh:
            line = line.strip()

            # NR % 2 == 0 only on seq lines in a fasta
            if NR % 2 == 0:
                seq = line

                # increment count of each seqs in counter on condition
                if len(seq) > 30:
                    seq_counter[seq] += 1

            # increment line number
            NR += 1

        # make dict for easy accesss
        common = dict(seq_counter.most_common(get_args().k))

        print('counts   seq')

        # make output look good
        for key in common:
            print(f'{common[key]}:  {key}')


# cache input file
infile = get_args().fasta

# print 10 most commone seqs
common_seqs(infile)
