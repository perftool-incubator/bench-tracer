#!/usr/bin/env python3
# -*- mode: python; indent-tabs-mode: nil; python-indent-level: 4 -*-
# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4 filetype=python

import argparse


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--duration", default=None)
    parser.add_argument("--tracer", default=None)
    parser.parse_known_args()


if __name__ == "__main__":
    main()
