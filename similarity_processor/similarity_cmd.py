""" File provide command line interface for the text similarity index processor """
import os
import sys
import argparse
sys.path.append(os.path.abspath(os.path.join
                                (os.path.dirname(__file__), os.pardir
                                 )))
from similarity_processor.similarity_io import SimilarityIO


def create_parser(args):
    """ Function which add the command line arguments required for the commandline input
    of text similarity index processor"""
    # Create the parser
    cos_parser = argparse.ArgumentParser(description='Text Similarity Index Processor')

    # Add the arguments
    cos_parser.add_argument('--path',
                            metavar='--p',
                            type=str,
                            help='the Input file path')

    cos_parser.add_argument('--uniqid',
                            metavar='--u',
                            type=str,
                            help='uniq id index(column) of the input file')

    cos_parser.add_argument('--colint',
                            metavar='--c',
                            type=str,
                            help='the col of interest')
    # ...Create your parser as you like...
    return cos_parser.parse_args(args)


if __name__ == '__main__':
    # Execute the parse_args() method
    ARGS = create_parser(sys.argv[1:])
    # Process the similarity with inputs provided
    SIM_IO_OBJ = SimilarityIO(ARGS.path, ARGS.uniqid, ARGS.colint, None)
    SIM_IO_OBJ.orchestrate_similarity()
