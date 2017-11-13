# nxgn_tools

This repository holds scripts I have written for working with next-generation sequencing (NGS) data. Manuals for each script are described below.

## Fasta_tools

**length_dist.py**

`length_dist.py` generates a read length frequency distribution from an input fasta file.

**fasta2line**

The `fasta2line.py` script converts a fasta file with multiple sequence lines per entry to a fasta file with one sequence line per entry.


## Kmer_tools


**knorm**

The `knorm.py` program normalizes reads based on kmer coverage, throwing out reads whose median kmer coverage is above the coverage limit. This program is meant to be run before `kspec.py`.

**kspec**

The `kspec.py` script generates a kmer distribution from a fastq file, sending kmer frequency-distribution data to an output file.


## alignment_tools

**count_stats.py**

This script generates two summary files after the alignment of RNA-seq reads to a reference genome using [STAR](https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf).

The first file that is generated `counts_per_gene.tsv` is a summary of counts/gene for each file of RNA-seq reads, these are meant to be used downstream for differential expression analysis.


The second file that is generated `count_stats.tsv`, contains four columns with the following contents:

| column     | content  |
| ---------- | ---------- |
| column 1  | File name |
| column 2  | Total reads per file |
| column 3  | Number uniquely mapped reads |
| column 4  | Number of reads mapped to gene models |
