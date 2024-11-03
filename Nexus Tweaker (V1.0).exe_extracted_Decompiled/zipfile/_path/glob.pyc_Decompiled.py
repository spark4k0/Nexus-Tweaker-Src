# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import re

def translate(pattern):
    return match_dirs(translate_core(pattern))

def match_dirs(pattern):
    """
    Ensure that zipfile.Path directory names are matched.

    zipfile.Path directory names always end in a slash.
    """
    return f'{pattern}[/]?'

def translate_core(pattern):
    """
    Given a glob pattern, produce a regex that matches it.

    >>> translate('*.txt')
    '[^/]*\\\\.txt'
    >>> translate('a?txt')
    'a.txt'
    >>> translate('**/*')
    '.*/[^/]*'
    """
    return ''.join(map(replace, separate(pattern)))

def separate(pattern):
    """
    Separate out character sets to avoid translating their contents.

    >>> [m.group(0) for m in separate('*.txt')]
    ['*.txt']
    >>> [m.group(0) for m in separate('a[?]txt')]
    ['a', '[?]', 'txt']
    """
    return re.finditer('([^\\[]+)|(?P<set>[\\[].*?[\\]])|([\\[][^\\]]*$)', pattern)

def replace(match):
    """
    Perform the replacements for a match from :func:`separate`.
    """
    return match.group('set') or re.escape(match.group(0)).replace('\\*\\*', '.*').replace('\\*', '[^/]*').replace('\\?', '.')