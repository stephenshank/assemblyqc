import json
import sys
import argparse


def dss_json_cleaner(input_json, output_json):
    with open(input_json) as input_json_file:
        raw = json.load(input_json_file)
    dss = raw['WrapperForJSONConversion']['DocumentSummarySet']
    clean = {
        'DocumentSummarySet': sum([
            dss[i]['DocumentSummary']
            for i in range(len(dss))
        ], [])
    }
    with open(output_json, 'w') as output_json_file:
        json.dump(clean, output_json_file)


DESCRIPTION = """
dss_json_cleaner - NCBI DocumentSummarySet post JSON conversion cleaner
By Stephen D. Shank, Ph. D.
sshank@temple.edu
Acme Computational Molecular Evolution Group
http://lab.hyphy.org/
"""


def cli():
    "Command line interface for DocumentSummarySet JSON cleaner."
    if len(sys.argv) == 1:
        print(DESCRIPTION)
        print("For more information: dss_json_cleaner --help")
        sys.exit(0)
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-i',
        '--input',
        help='input (JSON)',
        dest='input',
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
    dss_json_cleaner(args.input, args.output)


if __name__ == '__main__':
    cli()
