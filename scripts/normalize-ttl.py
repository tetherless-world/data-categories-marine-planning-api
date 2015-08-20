__author__ = 'szednik'

from rdflib import Literal, BNode, Namespace, URIRef, Graph, Dataset, RDF, RDFS, XSD
import rdflib.resource
import argparse


def main(file):
	g = Graph()
	g.parse(file, format="turtle")
	print(g.serialize(format="turtle"))


if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument('file', metavar='FILE', help='RDF file to load')

	args = parser.parse_args()
	main(file=args.file)
