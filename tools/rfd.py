#!/usr/bin/env python
# Run this from project root
import argparse
import os
import sys
from datetime import datetime

__module__ = sys.modules[__name__]

def main():
    # Parse CLI arguments
    parser = build_parser()
    args = parser.parse_args()
    print(args)

    func = f'subcommand_{args.subcommand}'
    if hasattr(__module__, func):
        try:
            exitcode = getattr(__module__, func)(args)
            exit(exitcode)
        except Exception as e:
            print(e)
            exit(-1)
    else:
        parser.print_help()
        exit(1)


def build_parser():
    # Initialize the parser
    parser = argparse.ArgumentParser(prog='rfd.py')
    subparsers = parser.add_subparsers(dest='subcommand', help='sub-command help')

    # Make subparser parser
    parser_make = subparsers.add_parser('make', help=getattr(__module__, 'subcommand_make').__doc__)

    # Return the parser
    return parser


def subcommand_make(args):
    """
    Make a new RFD
    """
    print('Fill out the information below to allocate a new RFD number.\n')
    
    # Generate the new RFD number
    num = len(os.listdir('./rfd'))
    rfd_id = f'{num:04d}'
    

    # Get metadata from user
    title = prompt('Enter a title')
    description = prompt('Enter a description')
    name = prompt('Author name')
    github = prompt('Author\'s GitHub username')
    tags = prompt('Tags (enter a comma-separated list)').split(',')
    tags = ['rfd'] + [ t.strip() for t in tags ]
    tags = [ t for t in tags if t != '' ]

    # Format output from prototype
    params = {
        'id': rfd_id,
        'title': title,
        'date': datetime.today().strftime('%Y-%m-%d'),
        'description': description,
        'name': name,
        'github': github,
        'tags': tags
    }
    prototype = open(os.path.join('prototypes', 'rfd-prototype.md')).read()
    output = prototype.format(**params)

    # Write new RFD 
    os.mkdir(os.path.join('rfd', rfd_id))
    with open(os.path.join('rfd', rfd_id, 'index.md'), 'w') as f:
        f.write(output)

    # Update the index
    fname = os.path.join('rfd', 'README.md')
    index = open(fname).read()
    index += '\n| {id} | created  | [RFD {id} {title}](./{id}/index.md) |'.format(**params)
    open(fname, 'w').write(index)
    print(bold(green('OK')))


class colors:
    magenta   = '\033[95m'
    blue      = '\033[94m'
    cyan      = '\033[96m'
    green         = '\033[92m'
    yellow        = '\033[93m'
    red           = '\033[91m'
    white         = '\033[97m'
    esc           = '\033[0m'
    bold          = '\033[1m'
    dull          = '\033[2m'
    italic        = '\033[3m'
    underline = '\033[4m'


def magenta(s):
    return f'{colors.magenta}{s}{colors.esc}'


def blue(s):
    return f'{colors.blue}{s}{colors.esc}'


def cyan(s):
    return f'{colors.cyan}{s}{colors.esc}'


def green(s):
    return f'{colors.green}{s}{colors.esc}'


def yellow(s):
    return f'{colors.yellow}{s}{colors.esc}'


def red(s):
    return f'{colors.red}{s}{colors.esc}'


def white(s):
    return f'{colors.white}{s}{colors.esc}'


def bold(s):
    return f'{colors.bold}{s}{colors.esc}'


def dull(s):
    return f'{colors.dull}{s}{colors.esc}'


def italic(s):
    return f'{colors.italic}{s}{colors.esc}'


def underline(s):
    return f'{colors.underline}{s}{colors.esc}'


def prompt(s, default=None):
    p = bold(dull('+ ')) + bold(cyan(s)) + bold(white(': '))
    return input(p)


if __name__ == '__main__':
    main()