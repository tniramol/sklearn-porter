# -*- coding: utf-8 -*-

from os.path import sep

from sklearn_porter.language.LanguageABC import LanguageABC


class C(LanguageABC):
    KEY = 'c'
    LABEL = 'C'

    DEPENDENCIES = ['gcc']
    TEMP_DIR = 'c'
    SUFFIX = 'c'

    # gcc tmp/estimator.c -std=c99 -lm -o tmp/estimator
    CMD_COMPILE = 'gcc {src_dir}' \
                  + sep + '{src_file} -std=c99 -lm -o {dest_dir}' \
                  + sep + '{dest_file}'

    # tmp/estimator <args>
    CMD_EXECUTE = '{dest_dir}' + sep + '{dest_file}'

    TEMPLATES = {
        'init':         '{type} {name} = {value};',

        # if/else condition:
        'if':           'if ({0} {1} {2}) {{',
        'else':         '} else {',
        'endif':        '}',

        # Basics:
        'indent':       '    ',
        'join':         '; ',
        'type':         '{0}',

        # Arrays:
        'in_brackets':  '{{{0}}}',
        # in ages[2] = {1, 2};
        'arr[]':        '{type} {name}[{n}] = {{{values}}};',
        'arr[][]':      '{type} {name}[{n}][{m}] = {{{values}}};',

        # Primitive data types:
        'int':          'int',
        'double':       'double'
    }
