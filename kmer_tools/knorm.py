#!/usr/bin/env python3.6

import argparse
from collections import defaultdict


def get_arguments():
    '''Define and return command line options.'''
    parser = argparse.ArgumentParser(
        prog='Kmer Normalization',
        description='This program removes reads from a fastq file\
                    whose median kmer coverage is above a set \
                    coverage limit')

    parser.add_argument('-c', '--covlimit',
                        help='specify coverage limit',
                        required=False, type=int)
    parser.add_argument('-i', '--infile',
                        help='specify input file (path)',
                        required=True,
                        type=argparse.FileType('rt',
                                               encoding='UTF-8'))
    parser.add_argument('-o', '--outfile',
                        help='specify output file (path)',
                        required=False,
                        type=argparse.FileType('wt',
                                               encoding='UTF-8'))
    parser.add_argument('-k', '--ksize',
                        help='specify kmer size (int)',
                        required=True, type=int, default=15)
    return parser.parse_args()


def median_func(li):
    '''Returns the median of a list of numbers'''
    li.sort()
    half = len(li) // 2
    if not len(li) % 2:
        return (li[half - 1] + li[half]) / 2.0
    return li[half]


args = get_arguments()

# Define Kmer size
kmer_size = args.ksize

# Define kmer coverage limit
coverage_lim = args.covlimit

# Define outfile
outfile = args.outfile.name

# Define input file
file = args.infile.name

# Initialize dict holding number of each kmer
kmer_dict = defaultdict(int)

# Initialize array holding kmer coverage
kmer_coverage = []

write = bool()

# Open file and extract kmer data
with open(file, 'r') as fh, open(outfile, 'w') as ot:
        NR = 0
        for line in fh:  # loop over lines in the file
            line = line.strip('\n')  # strip newline characters
            if NR % 4 == 0:
                head = line
            elif NR % 4 == 1:  # select only sequence lines
                seq = line

                for mer in range(len(seq)-kmer_size+1):
                    # kmerize each line and increment it's position
                    # kmer_dict
                    kmer_dict[seq[mer:kmer_size+mer]] += 1

                    kmer_coverage.append(seq[mer:kmer_size+mer])

                    # print reads whose median coverage is below the
                    # coverage limit
                kmer_coverage = [kmer_dict[v] for v in kmer_coverage]

                if coverage_lim > median_func(kmer_coverage):
                    write = bool(1)

            plus = fh.readline()
            NR += 1

            qual = fh.readline()
            NR += 1

            if write:
                ot.write(f'{head}\n{seq}\n{plus}\n{qual}')

            write = bool()

            # progress report!
            if NR % 10000 == 0:
                print(f"Processed line: {NR}")
