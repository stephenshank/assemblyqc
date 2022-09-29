import csv

import pysam


def extract_positions_from_bam(input_bam, output_csv):
    output_file = open(output_csv, 'w')
    csv_writer = csv.writer(output_file)
    header = (
        'name',
        'read_index',
        'mate_index',
        'read_start',
        'read_end',
        'mate_start',
        'mate_end'
    )
    csv_writer.writerow(header)
    af = pysam.AlignmentFile(input_bam)
    mate_hash = {}
    for read_index, read in enumerate(af.fetch()):
        if read.query_name in mate_hash:
            start, end, ind = mate_hash[read.query_name]
            del mate_hash[read.query_name]
            read_and_mate_locations = (
                read.query_name,
                ind,
                read_index,
                start,
                end,
                read.reference_start,
                read.reference_end
            )
            if None in read_and_mate_locations:
                continue
            csv_writer.writerow(read_and_mate_locations)
        else:
            mate_hash[read.query_name] = (
                read.reference_start, read.reference_end, read_index
            )
    output_file.close()


if __name__ == '__main__':
    accession = 'SRR10971381'
    #accession = 'SRR17309643'
    input_bam = 'data/%s/%s.bam' % (accession, accession)
    output_csv = 'data/%s/%s.csv' % (accession, accession)
    extract_positions_from_bam(input_bam, output_csv)
