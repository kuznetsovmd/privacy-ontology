#!/usr/bin/env python
import argparse
import sys

from env import env
from builders.manual.config import config as manual_conf
from builders.opp.config import config as opp_conf
from builders.annotations.config import config_annotated as annotated_conf
from builders.annotations.config import config_classified as classified_conf
from builders.classifiers.config import config as classifiers_conf
from queries.config import config as queries_conf

from builders.manual.builder import build as build_manual
from builders.opp.builder import build as build_opp
from builders.annotations.builder import build as build_annotations
from builders.classifiers.builder import train_classifier
from builders.classifiers.builder import eval_classifier
from queries.queries import exec as exec_queries


def main(args):
    if args.cmd == 'manual':
        build_manual(**manual_conf(**env()))
    if args.cmd == 'opp':
        build_opp(**opp_conf(**env()))
    if args.cmd == 'annotations':
        build_annotations(**annotated_conf(**env()))
    if args.cmd == 'classifiers':
        if args.train:
            for c in classifiers_conf(**env()):
                train_classifier(**c)
        if args.eval:
            for c in classifiers_conf(**env()):
                eval_classifier(**c)
            build_annotations(**classified_conf(**env()))
    if args.cmd == 'queries':
        exec_queries(**queries_conf(**env()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='privacy-ontology',
        description='Command line tool to control ontology framework'
    )

    parser.add_argument('cmd', help='One of: manual, annotations, classifiers, queries')
    parser.add_argument('-e', '--eval', default=False, action='store_true')
    parser.add_argument('-t', '--train', default=False, action='store_true')
    args = parser.parse_args()

    try:
        main(args)
        sys.exit(0)
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(130)
