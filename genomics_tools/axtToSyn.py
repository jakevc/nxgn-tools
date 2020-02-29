#!/usr/bin/env python3
"""
axtToSyn.py

Generates elongated synteny blocks from a pairwise alignment .axt file.
You can specify a min lastz alignment score to filter .axt file by 
the last filed. The min block length only considers elongated blocks 
larger than this length.

Jake VanCampen
vancampen@ohsu.edu
"""
import argparse

def get_args():
    '''Define and return command line arguments'''
    parser = argparse.ArgumentParser(
        prog='axtToSyn',
        description='Generates synteny blocks from pairwise genome \
        alignment .axt file by block elongation.')
    parser.add_argument('file',
                        help='Relative path to net.axt alignment file.',
                        type=str)
    parser.add_argument('outfile',
                        help='Path to output synteny blocks file.',
                        type=str,
                        default="synblocks.csv")
    parser.add_argument('s',
                        type=int,
                        help='Min alignment score to be considered for\
                                elongation (defalt: 1e6)',
                        default=1e6,
                        nargs='?'
                        )
    parser.add_argument('l',
                        type=int,
                        help='Min block len to be considered for\
                                elongation (defalt: 2e5)',
                        default=2e5,
                        nargs='?')
    return parser.parse_args()


def axtFilter(file, min_score):
    '''
    Generates alignment fields with
    min_score from .axt alignment file.
    '''
    fi=file
    with open(fi, 'r') as f:
        for l in f:
            l=l.strip().split(" ")
            # skip lines without len 9
            if len(l) != 9:
                continue
            # skip score less than min_score 
            elif int(l[8]) < min_score:
                continue
            else:
                yield(l[1:8])

def write_outfile(sp, outname):
    with open(outname, 'w') as of:
        for b in sp:
            of.write(",".join(b))
            of.write("\n")

def main():
    args=get_args()
    # initiate first pass 
    first_pass=[]
    file = args.file
    outfile = args.outfile
    min_len = args.l 
    min_score = args.s

    print(f"Using min alignment score {min_score}...")
    print(f"Using min block length {min_len}")

    # start the first block on the first line
    print("Elongating the synblocks on first pass...")
    block=next(axtFilter(file, min_score))
    for l in axtFilter(file, min_score):
        if block[0]==l[0] and block[3]==l[3] and block[6]==l[6]:
            # extend block in chromosome
            block[2]=l[2]
            block[5]=l[5]
        # min block len 
        elif int(block[5])-int(block[4]) > min_len:
            # add syn block 
            first_pass.append(block)
            # reset block
            block=l
        else:
            block=l

    print("Elongating the synblocks for a second pass...")
    first=True
    second_pass=[]
    s=first_pass[0]
    for fp in first_pass:
        if s[0]==fp[0] and s[3]==fp[3] and s[6]==fp[6]:
            # elongate block
            s[2]=fp[2]
            s[5]=fp[5]
        else:
            # append block and reset
            second_pass.append(s)
            s=fp

    # write synblocks 
    write_outfile(second_pass, outfile)
    # log stats
    nfirst=len(first_pass)
    nsecond=len(second_pass)
    print(f"{nfirst} synblocks after first pass\n{nsecond} synblocks after second pass.")

if __name__=="__main__":
    main()
