#!/usr/bin/env python3
'''
    generate_readme
    ---------------

    Dynamically generate README documentation from the API
    specification.
'''

import json
import rest
import os
import sys

# CONSTANTS
# ---------

DEV_HOME = os.path.dirname(os.path.realpath(__file__))
PROJECT_HOME = os.path.dirname(DEV_HOME)
NIS_HOME = os.path.join(PROJECT_HOME, 'nis')
README_MD_IN = os.path.join(DEV_HOME, 'README.md.in')
API_JSON = os.path.join(NIS_HOME, 'api.json')
README_MD = os.path.join(PROJECT_HOME, 'README.md')

# FUNCTIONS
# ---------


def fragment_escape(name):
    '''Escape symbols in header for a URL fragment.'''

    # insufficient, but will do for now...
    return name.replace('/', '')


def format_toc(name):
    '''Format resource for Table of Contents in markdown'''

    return '  - [{0}](#{1})'.format(name, fragment_escape(name))


def format_description(resource):
    '''Format API description from resource.'''

    description = '## {}'.format(resource.path)

    return description


def format_readme(root):
    '''Format README using data from the root.'''

    with open(README_MD_IN) as f:
        readme = f.read()

    toc = []
    description = []

    for resource in root.resources:
        toc.append(format_toc(resource.path))
        description.append(format_description(resource))

    import pdb; pdb.set_trace()
    return readme.format(
        version=root.version,
        api_table_of_contents='\n'.join(toc),
        api_description='\n\n'.join(description),
    )


def main():
    '''Dynamically generate README.'''

    with open(API_JSON) as f:
        root = rest.Root.from_json(f.read())

    readme = format_readme(root)
    with open(README_MD, 'w') as f:
        f.write(readme)


if __name__ == '__main__':
    main()
