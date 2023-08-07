import sys
import argparse
import warnings


empty_xml = '''<WrapperForJSONConversion>
    <DocumentSummarySet>
        <DocumentSummary>
        </DocumentSummary>
    </DocumentSummarySet>
</WrapperForJSONConversion>'''


def dss_xml_cleaner(input_xml, output_xml):
    xml_input_file = open(input_xml)
    xml_output_file = open(output_xml, 'w')
    try:
        for _ in range(2):
            line = next(xml_input_file)
            xml_output_file.write(line)
        xml_output_file.write('<WrapperForJSONConversion>\n')
        for line in xml_input_file:
            xml_output_file.write('  '+line)
        xml_output_file.write('</WrapperForJSONConversion>\n')
    except StopIteration:
        warnings.warn('proceeding as though XML file were empty')
        xml_output_file.write(empty_xml)
    xml_input_file.close()
    xml_output_file.close()


DESCRIPTION = """
dss_xml_cleaner - NCBI DocumentSummarySet XML cleaner for Python parsing
By Stephen D. Shank, Ph. D.
sshank@temple.edu
Acme Computational Molecular Evolution Group
http://lab.hyphy.org/
"""


def cli():
    "Command line interface for DocumentSummarySet XML cleaner."
    if len(sys.argv) == 1:
        print(DESCRIPTION)
        print("For more information: dss_xml_cleaner --help")
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
        help='output (XML)',
        dest='output',
        required=True
    )
    args = parser.parse_args()
    dss_xml_cleaner(args.input, args.output)


if __name__ == '__main__':
    cli()
