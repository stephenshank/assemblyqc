import json
import sys
import argparse

import xmltodict


def xml_to_json(xml_filename, json_filename):
    with open(xml_filename) as xml_file:
        xml = xml_file.read()
    converted = xmltodict.parse(xml)
    with open(json_filename, "w") as json_file:
        json.dump(converted, json_file, indent=2)


DESCRIPTION = """
xml_to_json - A simple XML to JSON converter
By Stephen D. Shank, Ph. D.
sshank@temple.edu
Acme Computational Molecular Evolution Group
http://lab.hyphy.org/
"""


def cli():
    "Command line interface for XML to JSON conversion."
    if len(sys.argv) == 1:
        print(DESCRIPTION)
        print("For more information: xmltojson --help")
        sys.exit(0)
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-i',
        '--input',
        help='input (XML)',
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
    xml_to_json(args.input, args.output)


if __name__ == '__main__':
    cli()
