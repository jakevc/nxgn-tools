# nxgn_tools

This repository holds scripts I have written for working with next-generation sequencing (NGS) data. Manuals for each script are described below.

## Fasta_tools

**fasta2line**

The `fasta2line.py` script converts a fasta file with multiple sequence lines per entry to a fasta file with one sequence line per entry.


## Kmer_tools


**knorm**

The `knorm.py` program normalizes reads based on kmer coverage, throwing out reads whose median kmer coverage is above the coverage limit. This program is meant to be run before `kspec.py`.

**kspec**

The `kspec.py` script generates a kmer distribution from a fastq file, sending kmer frequency-distribution data to an output file.
