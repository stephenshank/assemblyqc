import pysam
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


# operations
MATCH = 0
INSERTION = 1
DELETION = 2
SKIP = 3
SOFT_CLIP = 4
HARD_CLIP = 5
CPAD = 6
EQUAL = 7
DIFF = 8
CBACK = 9


def clean_contig(read):
    operations_to_keep = set([
        MATCH, INSERTION
    ])
    operations_to_skip = set([
        DELETION, SOFT_CLIP
    ])
    position = 0
    chunks = []
    not_supported_error_message = 'Operation not supported... aborting!'
    for cigartuple in read.cigartuples:
        operation, length = cigartuple
        if operation in operations_to_keep:
            chunks += [read.query[position: position+length]]
        else:
            is_supported = operation in operations_to_skip
            assert is_supported, not_supported_error_message
    sequence = Seq(''.join(chunks))
    return SeqRecord(id='reassembled', seq=sequence, description='')


def pluck_best_contig(alignment_file):
    best_count = -1
    match_operation = 0
    for read in alignment_file.fetch():
        count = sum([
            cigartuple[1]
            for cigartuple in read.cigartuples
            if cigartuple[0] == match_operation
        ])
        if count > best_count:
            best_count = count
            best = read
    print('Plucking %s with %d aligned positions.' % (best.query_name, best_count) )
    return clean_contig(best)


def pluck_best_contig_io(input_bam, output_fasta):
    alignment_file = pysam.AlignmentFile(input_bam)
    record = pluck_best_contig(alignment_file)
    SeqIO.write(record, output_fasta, 'fasta')


if __name__ == '__main__':
    bam_filepath = 'data/SRR7170717/SRR7170717-contigs.bam'
    alignment_file = pysam.AlignmentFile(bam_filepath)
    pluck_best_contig(alignment_file)
