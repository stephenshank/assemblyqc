import json

import pysam


def extract_positions_from_bam(input_bam, output_json):
    af = pysam.AlignmentFile(input_bam)
    mate_hash = {}
    location_dict = {}
    for read_index, read in enumerate(af.fetch()):
        if read.query_name in mate_hash:
            start, end, ind = mate_hash[read.query_name]
            del mate_hash[read.query_name]
            locations = (start, end, read.reference_start, read.reference_end)
            if None in locations:
                continue
            key = '%d-%d-%d-%d' % locations
            location_dict[key] = (ind, read_index)
        else:
            mate_hash[read.query_name] = (
                read.reference_start, read.reference_end, read_index
            )
    with open(output_json, 'w') as f:
        json.dump(location_dict, f, indent=2)


if __name__ == '__main__':
    accession = 'SRR10971381'
    #accession = 'SRR17309643'
    input_bam = 'data/%s/%s.bam' % (accession, accession)
    output_json = 'data/%s/%s.json' % (accession, accession)
    extract_positions_from_bam(input_bam, output_json)
