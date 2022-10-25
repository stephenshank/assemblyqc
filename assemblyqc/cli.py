import argparse

from pluck import *


def pluck_best_contig_cli():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "-b",
        "--bam",
        help="path to input bam",
        dest="bam",
        required=True
    )

    parser.add_argument(
        "-f",
        "--fasta",
        help="path to output fasta file",
        dest="fasta",
        required=True
    )

    args = parser.parse_args()
    pluck_best_contig_io(args.bam, args.fasta)


if __name__ == '__main__':
    pluck_best_contig_cli()
