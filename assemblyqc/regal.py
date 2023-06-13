import json
import sys
import argparse

from Bio import SeqIO


def get_contig_boundaries(input_bed, input_reference):
    bed = open(input_bed)
    contig_stats = {}
    previous_chromosome = None
    for line in bed:
        chromosome, start, end, coverage = extract_bedcov_line(line)
        if start == 0 and end == 0 and coverage == 0:
            # pathological line?
            continue
        new_chromosome = chromosome != previous_chromosome
        if new_chromosome:
            contig_stats[chromosome] = {'contigs': [[start, end]]}
        elif coverage == 0:
            # new_contig
            contig_stats[chromosome]['contigs'].append([end, None])
        else:
            contig_stats[chromosome]['contigs'][-1][1] = end
        previous_chromosome = chromosome
    bed.close()
    for record in SeqIO.parse(input_reference, 'fasta'):
        contig_stats[record.id]['length'] = len(record)
        last_contig = contig_stats[record.id]['contigs'][-1]
        if last_contig[1] is None:
            contig_stats[record.id]['contigs'].pop()
    
    return contig_stats


def extract_bedcov_line(line):
    split = line.split('\t')
    chromosome = split[0]
    start = int(split[1])
    end = int(split[2])
    coverage = int(split[3])
    return chromosome, start, end, coverage


DESCRIPTION = """
regal - Read-based Evaluation of Genome Assemblies Library
By Stephen D. Shank, Ph. D.
sshank@temple.edu
Acme Computational Molecular Evolution Group
http://lab.hyphy.org/
"""

def regal_cli():
    "Full command line interface function."
    if len(sys.argv) == 1:
        print(DESCRIPTION)
        print("For more information: regal --help")
        sys.exit(0)
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-c',
        '--coverage',
        help='coverage (BED)',
        dest='coverage',
        required=True
    )
    parser.add_argument(
        '-a',
        '--assembly',
        help='assembly (FASTA)',
        dest='assembly',
        required=True
    )
    parser.add_argument(
        '-o',
        '--output',
        help='output (JSON)',
        dest='output',
        required=True
    )
    args = parser.parse_args()
    regal = get_contig_boundaries(args.coverage, args.assembly)
    with open(args.output, 'w') as json_file:
        json.dump(regal, json_file, indent=2)


if __name__ == '__main__':
    regal_cli()
