from Bio import SeqIO
import numpy as np


def qc(pairwise_alignment_path):
    pairwise_alignment = SeqIO.parse(pairwise_alignment_path, 'fasta')
    seq1, seq2 = list(pairwise_alignment)
    seq1np = np.array(list(str(seq1.seq)), dtype='<U1')
    seq2np = np.array(list(str(seq2.seq)), dtype='<U1')
    n_sites = len(seq1)
    matched_bases = (seq1np == seq2np).sum()
    percent_identity = matched_bases / n_sites
    return {
        'percent_identity': percent_identity
    }


if __name__ == '__main__':
    print(qc('./data/SRR10971381/megahit-reassembled.fasta'))
