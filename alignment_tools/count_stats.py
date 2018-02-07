#!/usr/bin/env python3.6

'''
This script generates two files of statistics after the alignment of paired-end
RNA-seq reads to a reference genome using STAR. The first `counts_per_gene.tsv`
contains one column representing the genes in the reference genome. Subsequent
columns contain gene counts for each file of aligned reads the aligned reads.

The second file `count_stats.tsv` generate a summary of mapping statistics for
each file of aligned reads.

This script is meant to be run from inside a directory containing the output of
STAR's mapping step.
'''

import pandas as pd
import os

# Generate a table of counts for each gene, for each file.

# firstline case
firstone = True

# loop over all files in working directory
for file in os.listdir():
    filename = file
    if firstone & filename.endswith('ReadsPerGene.out.tab'):
        # grab the filename
        name = filename.split('_L')[0]
        data = pd.read_csv(file, delimiter='\t',
                           header=None, index_col=0,
                           usecols=(0, 3), names=['gene', name])
        # exit firstline case
        firstone = False

    elif filename.endswith('ReadsPerGene.out.tab'):
        name = filename.split('_L')[0]

        # joine each files counts on the gene column
        data = data.join(pd.read_csv(
                         file, delimiter='\t', header=None,
                         index_col=0, usecols=(0, 3),
                         names=['gene', name]))

# write file to output
data.to_csv('counts_per_gene.tsv', sep='\t')


# Generate mapping statistics for each file

# open file for writing
with open('count_stats.tsv', 'w') as fh:
    # write header
    fh.write('file\ttotal_reads\tuniq_reads\treads_on_genes\n')

    # loop over directory
    for file in os.listdir():

        # if it's the log file
        if file.endswith('Log.final.out'):

            # grab the file name
            name = file.split('_L')[0]
            # retain file
            fi = pd.read_csv(
                    file, delimiter='\t', header=None, names=['key', 'value']
                    )
            # retain stats of interest
            fi = fi[
                    fi['key'].str.contains('Number of input reads') |
                    fi['key'].str.contains('Uniquely mapped reads number')
                    ]
            # set index to first column
            fi.set_index('key', inplace=True)

            # cache stats from data frame
            total_reads = fi.value[0]
            uniq_reads = fi.value[1].strip()

            # loop over dir to count reads/gene-model
            for counts in os.listdir():
                if counts.endswith('ReadsPerGene.out.tab'):

                    # to reference current filename
                    if name in counts:
                        current = pd.read_csv(
                                    counts, header=None, delimiter='\t')

                        # select 4th column of 'ReadsPerGene.out.tab'
                        num_reads_on_gene = sum(current[4:][3])

                        # write to output file
                        fh.write(f'{name}\t{total_reads}\t\
                                    {uniq_reads}\t{num_reads_on_gene}\n')
