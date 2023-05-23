import csv


def get_contig_boundaries(input_pileup, output_contig_stats):
    pileup = open(input_pileup)
    contig_stats = []
    start = None
    end = None
    for line in pileup:
        position = extract_pileup_line(line)
        if start is None:
            start = position
            end = position
        elif position == end + 1:
            end = position
        else:
            contig_stats.append([start, end])
            start = position
            end = position
    if start is not None:
        contig_stats.append([start, end])
    pileup.close()
    with open(output_contig_stats, 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['start', 'end'])
        for contig in contig_stats:
            csv_writer.writerow(contig)


def extract_pileup_line(line):
    split = line.split('\t')
    position = int(split[1])
    return position


if __name__ == '__main__':
    #input_pileup = 'data/pileup-test.tsv'
    input_pileup = 'data/Galaxy16-[Samtools_mpileup_on_data_1_and_data_15].pileup'
    output_contig_stats = 'data/contig_stats.csv'
    get_contig_boundaries(input_pileup, output_contig_stats)
