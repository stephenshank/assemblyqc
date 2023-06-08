import json


def get_contig_boundaries(input_bed, output_contig_stats):
    bed = open(input_bed)
    contig_stats = {}
    previous_chromosome = None
    for line in bed:
        chromosome, start, end, coverage = extract_pileup_line(line)
        if start == 0 and end == 0 and coverage == 0:
            # pathological line
            continue
        if previous_chromosome is None:
            # just beginning
            contig_stats[chromosome] = [[start, end]]
        elif chromosome != previous_chromosome:
            # new_chromosome
            contig_stats[chromosome] = [[start, end]]
        elif coverage == 0:
            # new_contig
            contig_stats[chromosome].append([end, None])
        else:
            contig_stats[chromosome][-1][1] = end
        previous_chromosome = chromosome
    bed.close()
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
    input_coverage = 'data/test.bed'
    output_contig_stats = 'data/contig_stats.json'
    get_contig_boundaries(input_coverage, output_contig_stats)
