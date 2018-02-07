#! /usr/bin/env python3.6

'''
This script looks up the annotation gene name from a
file containing chromosome and position.
'''

# move around a directory
import argparse
from collections import defaultdict


def get_args():
    '''Define and return command line arguments'''
    parser = argparse.ArgumentParser(
        prog='annotation lookup',
        description='Looks up the annotation gene name from a\
        file containing chromosome and position outputs a file with \
        the gene name added')
    parser.add_argument('chrom_file', type=str,
                        help='chromosome file (path)')
    parser.add_argument('ann_file', type=str,
                        help='annotation file (path)')
    return parser.parse_args()


# grab the chrfile and the annotation file
chrfile = get_args().chrom_file
annfile = get_args().ann_file
outfile = chrfile[-4]+'_annot.txt'


# open chromosome file
with open(chrfile, 'r') as fh:
    poslist = []
    chr_dct = defaultdict(int)
    for line in fh:

        # strip and split on tab
        line = line.strip().split()

        # determine dict of chromosome, position pairs,
        # accessing keys of this dict removes dups
        chr_dct[(line[0], int(line[1]))] += 1

        # list all positions to determine range of positions
        poslist.append(int(line[1]))

        # store the range of positions to lookup in annotation
        window = (int(min(poslist)), int(max(poslist)))


# open annotation file
with open(annfile, 'r') as ah:

    anot_dict = {}
    for line in ah:

        # split on tabs
        line = line.strip()

        # line split on tab
        spl = line.split()

        # chromosome for that line
        chrm = spl[0]

        # remove semi-colon from end and quotes
        gene_name = spl[17][0:-1].replace('"', '')

        # base pair range for that line
        ann_region = (int(spl[3]), int(spl[4]))

        # if the annotation is in the region we care about
        if ann_region[0] >= window[0] and ann_region[1] <= window[1]:
            # make dict for search
            anot_dict[(chrm, ann_region)] = gene_name


# open file to write to
with open(outfile, 'w') as of:

    # loop over query keys
    for key in chr_dct:

        # and each annotation
        for k in anot_dict:

            # find chromosome names that match annotation entries,
            # whose position is in the window
            if key[0] in k[0] and k[1][0] <= key[1] <= k[1][1]:

                # write that entry to a new file, tab separate
                of.write(f'{key[0]}\t{key[1]}\t{anot_dict[k]}\n')
