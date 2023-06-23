import unittest
import json

from assemblyqc import calculate_n_and_l


class TestCalculateNAndL(unittest.TestCase):
    def test_main(self):
        with open('data/candida.json') as json_file:
            all_contig_stats = json.load(json_file)
        single_contig_stats = all_contig_stats["NC_032089.1"]
        n, l = calculate_n_and_l(single_contig_stats, 50)
        self.assertTrue(n > 0)
        self.assertTrue(l > 0)
