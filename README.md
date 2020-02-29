# nxgn_tools

This repository holds scripts I have written for working with next-generation sequencing (NGS) data. Manuals for each script are described below.

## Genomics_tools 

axtToSyn.py 

This script elongates synteny blocks from a pairwise whole genome alignment, chained and netted and in the .axt file format.

```
./axtToSyn.py -h
usage: axtToSyn [-h] file outfile [s] [l]

Generates synteny blocks from pairwise genome alignment .axt file by block
elongation.

positional arguments:
  file        Relative path to net.axt alignment file.
  outfile     Path to output synteny blocks file.
  s           Min alignment score to be considered for elongation (defalt:
              1e6)
  l           Min block len to be considered for elongation (defalt: 2e5)

optional arguments:
  -h, --help  show this help message and exit
```



## Fasta_tools

**length_dist.py**

`length_dist.py` generates a read length frequency distribution from an input fasta file.

**fasta2line**

The `fasta2line.py` script converts a fasta file with multiple sequence lines per entry to a fasta file with one sequence line per entry.

**common_seqs.py -h** 
usage: common_seqs [-h] fasta [k]

Determins k most common sequences with length greater than 30nts from fasta
file, returns seq and counts

positional arguments:
  fasta       input fasta file (path)
  k           Specify the k most common seqs. Default: 10

optional arguments:
  -h, --help  show this help message and exit

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

**annotation_lookup.py**

usage: annotation lookup [-h] chrom_file ann_file

Looks up the annotation gene name from a file containing chromosome and
position outputs a file with the gene name added

positional arguments:
  chrom_file  chromosome file (path)
  ann_file    annotation file (path)

optional arguments:
  -h, --help  show this help message and exit

## Coding tasks

**report_fastq.py -h**

usage: report_fastq.py [-h] [--help] crawl_dir

This script recursively searches through a directory to look for fastq
files and prints out the file name with the percent of sequences in that
file that are greater than 30 nucleotides long.

-------------------
positional argument:
    crawl_dir   relative or abs path to directory

optional arguments:
    -h, --help  print this help message and exit






