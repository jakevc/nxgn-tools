#!/usr/bin/env python3.6

import argparse
from collections import defaultdict


def get_arguments():
    '''Define and return command line options.'''
    parser = argparse.ArgumentParser(
        prog='Kmer Spec',
        description='This program calculates kmer distribution of a\
                    fastq file and writes data to --outfile')

    parser.add_argument('-k', '--kmersize', help='specify kmer size (int)',
                        required=True, type=int)
    parser.add_argument('-i', '--infile', help='specify input file (path)',
                        required=True,
                        type=argparse.FileType('rt', encoding='UTF-8 '))
    parser.add_argument('-o', '--outfile', help='specify output file (path)',
                        required=True,
                        type=argparse.FileType('wt', encoding='UTF-8 '))
    return parser.parse_args()


def sort_dec(unsorted_dict):
    '''Sort the values of a dictionary on decending values.'''
    return dict(sorted(unsorted_dict.items(), key=(lambda x: (x[1])),
                reverse=True))


# return command line options
args = get_arguments()

# specify kmer size by command line option -f
kmer_size = args.kmersize

# specify files by command line option -i , -o
file = args.infile.name

outfile = args.outfile.name

# define dictonary holding number of occurances of each kmer
kmer_dict = defaultdict(int)

# define dictonary counting kmers of each frequency
kmer_freq = defaultdict(int)

# open file and extract kmer data
with open(file, 'r') as fh:
        NR = 0
        for line in fh:  # loop over lines in the file
            line = line.strip('\n')  # strip newline characters
            if NR % 4 == 1:  # select only sequence lines
                for mer in range(len(line)-kmer_size+1):
                    # kmerize each line and increment it's position
                    # store in kmer_dict
                    kmer_dict[line[mer:kmer_size+mer]] += 1
            NR += 1
            if NR % 10000 == 0:
                print(f"Processed line: {NR}")

# number of possible kmers for each line
kmer_cnt = len(line) - (kmer_size + 1)

# sort vlaues of dict by key
kmer_dict = sort_dec((kmer_dict))

# generate dictonary containing number of occurances for number of kmers
for v in kmer_dict.values():
    kmer_freq[v] += 1


# open file to write output
with open(outfile, 'w') as ofi:
    # print dict, sorted on keys
    ofi.write('Times Kmer occurs'+'\t'+'Number of Kmers\n')
    for k, v in sorted(kmer_freq.items()):
            ofi.write(f'{k}\t{v}\n')
