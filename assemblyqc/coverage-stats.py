import json

from Bio import SeqIO


def get_contig_boundaries(input_bed, input_reference, output_contig_stats):
    bed = open(input_bed)
    contig_stats = {}
    previous_chromosome = None
    for line in bed:
        chromosome, start, end, coverage = extract_pileup_line(line)
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

    with open(output_contig_stats, 'w') as json_file:
        json.dump(contig_stats, json_file, indent=2)


def extract_pileup_line(line):
    split = line.split('\t')
    chromosome = split[0]
    start = int(split[1])
    end = int(split[2])
    coverage = int(split[3])
    return chromosome, start, end, coverage


if __name__ == '__main__':
    input_coverage = 'data/candida.bed'
    output_contig_stats = 'data/candida.json'
    input_reference = 'data/candida.fasta'
    get_contig_boundaries(input_coverage, input_reference, output_contig_stats)
