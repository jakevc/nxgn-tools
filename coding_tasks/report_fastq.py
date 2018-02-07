#! /usr/bin/env python3.6

'''
This script recursively searches through a directory to look for fastq
files and prints out the file name with the percent of sequences in that
file that are greater than 30 nucleotides long.
'''

# move around a directory
import sys
import os


def get_fastq_paths(query_dir):
    '''recursively walks the directory 'query_dir', returns all fq files
    '''

    # show helpful error if you do not pass directory to script
    if not os.path.isdir(query_dir):
        raise ValueError(f'{query_dir} is not a directory')

    # walk the current directory
    walk = os.walk(query_dir, topdown=False)

    # initialize list of file paths
    fastq_list = []

    # determine paths dirs and files
    for path, dirs, files in walk:

        # look at each file
        for name in files:

            # chose names with that end with fastq of fq
            if name.endswith('fq') or name.endswith('fastq'):

                # append relative path to file_list
                fastq_list.append(os.path.join(path, name))

            # forget about the other files
            else:
                pass

    return fastq_list


def get_percent_over_thirty(file):
    # open file to loop through the lines
    with open(file, 'r') as fh:

        # counts of seqs with length > 30 nt
        over_thirty = 0

        # line count
        NR = 1

        for line in fh:
            line = line.strip()

            # line number % 4 is only equal to 2 on seq lines
            if NR % 4 == 2:
                seq = line

                # increment over_thirty count if true
                if len(seq) > 30:
                    over_thirty += 1
            NR += 1

        # assume seq number is 1/4 the number of lines
        seq_count = NR/4

        # calculate percent of seqs over 30nt long
        per_over_thirty = round((over_thirty/seq_count) * 100, 2)

        # only retain file name from full path
        file = file.split('/')[-1]

        # print result to console
        print(f'{file} {per_over_thirty}')


# raise helpful error if you pass no argument
try:
    walk_dir = sys.argv[1]
except:
    raise ValueError('No directory argument found')

if sys.argv[1] == '-h' or sys.argv[1] == '-help':
    print('''
usage: report_fastq.py [-h] [--help] crawl_dir

This script recursively searches through a directory to look for fastq
files and prints out the file name with the percent of sequences in that
file that are greater than 30 nucleotides long.

-------------------
positional argument:
    crawl_dir   relative or abs path to directory

optional arguments:
    -h, --help  print this help message and exit
''')
    sys.exit(0)

# call the function to get the list of files in the walk
fastq_list = get_fastq_paths(walk_dir)

# print seqs over thirty nt to the console
for file in fastq_list:
    get_percent_over_thirty(file)
