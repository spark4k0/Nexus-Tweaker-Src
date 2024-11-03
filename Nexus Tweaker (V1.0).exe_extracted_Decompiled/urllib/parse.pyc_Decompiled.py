# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""Parse (absolute and relative) URLs.\n\nurlparse module is based upon the following RFC specifications.\n\nRFC 3986 (STD66): \"Uniform Resource Identifiers\" by T. Berners-Lee, R. Fielding\nand L.  Masinter, January 2005.\n\nRFC 2732 : \"Format for Literal IPv6 Addresses in URL\'s by R.Hinden, B.Carpenter\nand L.Masinter, December 1999.\n\nRFC 2396:  \"Uniform Resource Identifiers (URI)\": Generic Syntax by T.\nBerners-Lee, R. Fielding, and L. Masinter, August 1998.\n\nRFC 2368: \"The mailto URL scheme\", by P.Hoffman , L Masinter, J. Zawinski, July 1998.\n\nRFC 1808: \"Relative Uniform Resource Locators\", by R. Fielding, UC Irvine, June\n1995.\n\nRFC 1738: \"Uniform Resource Locators (URL)\" by T. Berners-Lee, L. Masinter, M.\nMcCahill, December 1994\n\nRFC 3986 is considered the current standard and any future changes to\nurlparse module should conform with it.  The urlparse module is\ncurrently not entirely compliant with this RFC due to defacto\nscenarios for parsing, and for backward compatibility purposes, some\nparsing quirks from older RFCs are retained. The testcases in\ntest_urlparse.py provides a good indicator of parsing behavior.\n\nThe WHATWG URL Parser spec should also be considered.  We are not compliant with\nit either due to existing user code API behavior expectations (Hyrum\'s Law).\nIt serves as a useful guide when making changes.\n"""
from collections import namedtuple
global _hextobyte  # inserted
global _portprog  # inserted
global _hostprog  # inserted
global _typeprog  # inserted
import functools
import math
import re
import types
import warnings
import ipaddress
__all__ = ['urlparse', 'urlunparse', 'urljoin', 'urldefrag', 'urlsplit', 'urlunsplit', 'urlencode', 'parse_qs', 'parse_qsl', 'quote', 'quote_plus', 'quote_from_bytes', 'unquote', 'unquote_plus', 'unquote_to_bytes', 'DefragResult', 'ParseResult', 'SplitResult', 'DefragResultBytes', 'ParseResultBytes', 'SplitResultBytes']
uses_relative = ['', 'ftp', 'http', 'gopher', 'nntp', 'imap', 'wais', 'file', 'https', 'shttp', 'mms', 'prospero', 'rtsp', 'rtsps', 'rtspu', 'sftp', 'svn', 'svn+ssh', 'ws', 'wss']
uses_netloc = ['', 'ftp', 'http', 'gopher', 'nntp', 'telnet', 'imap', 'wais', 'file', 'mms', 'https', 'shttp', 'snews', 'prospero', 'rtsp', 'rtsps', 'rtspu', 'rsync', 'svn', 'svn+ssh', 'sftp', 'nfs', 'git', 'git+ssh', 'ws', 'wss', 'itms-services']
uses_params = ['', 'ftp', 'hdl', 'prospero', 'http', 'imap', 'https', 'shttp', 'rtsp', 'rtsps', 'rtspu', 'sip', 'sips', 'mms', 'sftp', 'tel']
non_hierarchical = ['gopher', 'hdl', 'mailto', 'news', 'telnet', 'wais', 'imap', 'snews', 'sip', 'sips']
uses_query = ['', 'http', 'wais', 'imap', 'https', 'shttp', 'mms', 'gopher', 'rtsp', 'rtsps', 'rtspu', 'sip', 'sips']
uses_fragment = ['', 'ftp', 'hdl', 'http', 'gopher', 'news', 'nntp', 'wais', 'https', 'shttp', 'snews', 'file', 'prospero']
scheme_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-.'
_WHATWG_C0_CONTROL_OR_SPACE = '\x00\a\b\t\n\v\f\r '
_UNSAFE_URL_BYTES_TO_REMOVE = ['\t', '\r', '\n']

def clear_cache():
    """Clear internal performance caches. Undocumented; some tests want it."""  # inserted
    urlsplit.cache_clear()
    _byte_quoter_factory.cache_clear()
_implicit_encoding = 'ascii'
_implicit_errors = 'strict'

def _noop(obj):
    return obj

def _encode_result(obj, encoding=_implicit_encoding, errors=_implicit_errors):
    return obj.encode(encoding, errors)

def _decode_args(args, encoding=_implicit_encoding, errors=_implicit_errors):
    return tuple((x.decode(encoding, errors) if x else '' for x in args))

def _coerce_args(*args):
    str_input = isinstance(args[0], str)
    for arg in args[1:]:
        if arg and isinstance(arg, str)!= str_input:
            raise TypeError('Cannot mix str and non-str arguments')
    else:  # inserted
        if str_input:
            return args + (_noop,)
        return _decode_args(args) + (_encode_result,)

class _ResultMixinStr(object):
    """Standard approach to encoding parsed results from str to bytes"""
    __slots__ = ()

    def encode(self, encoding='ascii', errors='strict'):
        return self._encoded_counterpart(*(x.encode(encoding, errors) for x in self))

class _ResultMixinBytes(object):
    """Standard approach to decoding parsed results from bytes to str"""
    __slots__ = ()

    def decode(self, encoding='ascii', errors='strict'):
        return self._decoded_counterpart(*(x.decode(encoding, errors) for x in self))

class _NetlocResultMixinBase(object):
    """Shared methods for the parsed result objects containing a netloc element"""
    __slots__ = ()

    @property
    def username(self):
        return self._userinfo[0]

    @property
    def password(self):
        return self._userinfo[1]

    @property
    def hostname(self):
        hostname = self._hostinfo[0]
        if not hostname:
            return
        separator = '%' if isinstance(hostname, str) else b'%'
        hostname, percent, zone = hostname.partition(separator)
        return hostname.lower() + percent + zone

    @property
    def port(self):
        port = self._hostinfo[1]
        if port is not None:
            if port.isdigit() and port.isascii():
                port = int(port)
            else:  # inserted
                raise ValueError(f'Port could not be cast to integer value as {port!r}')
            if not 0 <= port <= 65535:
                raise ValueError('Port out of range 0-65535')
        return port
    __class_getitem__ = classmethod(types.GenericAlias)

class _NetlocResultMixinStr(_NetlocResultMixinBase, _ResultMixinStr):
    __slots__ = ()

    @property
    def _userinfo(self):
        netloc = self.netloc
        userinfo, have_info, hostinfo = netloc.rpartition('@')
        if have_info:
            username, have_password, password = userinfo.partition(':')
            if not have_password:
                password = None
            return (username, password)
        username = password = None
        return (username, password)

    @property
    def _hostinfo(self):
        netloc = self.netloc
        _, _, hostinfo = netloc.rpartition('@')
        _, have_open_br, bracketed = hostinfo.partition('[')
        if have_open_br:
            hostname, _, port = bracketed.partition(']')
            _, _, port = port.partition(':')
        else:  # inserted
            hostname, _, port = hostinfo.partition(':')
        if not port:
            port = None
        return (hostname, port)

class _NetlocResultMixinBytes(_NetlocResultMixinBase, _ResultMixinBytes):
    __slots__ = ()

    @property
    def _userinfo(self):
        netloc = self.netloc
        userinfo, have_info, hostinfo = netloc.rpartition(b'@')
        if have_info:
            username, have_password, password = userinfo.partition(b':')
            if not have_password:
                password = None
            return (username, password)
        username = password = None
        return (username, password)

    @property
    def _hostinfo(self):
        netloc = self.netloc
        _, _, hostinfo = netloc.rpartition(b'@')
        _, have_open_br, bracketed = hostinfo.partition(b'[')
        if have_open_br:
            hostname, _, port = bracketed.partition(b']')
            _, _, port = port.partition(b':')
        else:  # inserted
            hostname, _, port = hostinfo.partition(b':')
        if not port:
            port = None
        return (hostname, port)
_DefragResultBase = namedtuple('DefragResult', 'url fragment')
_SplitResultBase = namedtuple('SplitResult', 'scheme netloc path query fragment')
_ParseResultBase = namedtuple('ParseResult', 'scheme netloc path params query fragment')
_DefragResultBase.__doc__ = '\nDefragResult(url, fragment)\n\nA 2-tuple that contains the url without fragment identifier and the fragment\nidentifier as a separate argument.\n'
_DefragResultBase.url.__doc__ = 'The URL with no fragment identifier.'
_DefragResultBase.fragment.__doc__ = '\nFragment identifier separated from URL, that allows indirect identification of a\nsecondary resource by reference to a primary resource and additional identifying\ninformation.\n'
_SplitResultBase.__doc__ = '\nSplitResult(scheme, netloc, path, query, fragment)\n\nA 5-tuple that contains the different components of a URL. Similar to\nParseResult, but does not split params.\n'
_SplitResultBase.scheme.__doc__ = 'Specifies URL scheme for the request.'
_SplitResultBase.netloc.__doc__ = '\nNetwork location where the request is made to.\n'
_SplitResultBase.path.__doc__ = '\nThe hierarchical path, such as the path to a file to download.\n'
_SplitResultBase.query.__doc__ = '\nThe query component, that contains non-hierarchical data, that along with data\nin path component, identifies a resource in the scope of URI\'s scheme and\nnetwork location.\n'
_SplitResultBase.fragment.__doc__ = '\nFragment identifier, that allows indirect identification of a secondary resource\nby reference to a primary resource and additional identifying information.\n'
_ParseResultBase.__doc__ = '\nParseResult(scheme, netloc, path, params, query, fragment)\n\nA 6-tuple that contains components of a parsed URL.\n'
_ParseResultBase.scheme.__doc__ = _SplitResultBase.scheme.__doc__
_ParseResultBase.netloc.__doc__ = _SplitResultBase.netloc.__doc__
_ParseResultBase.path.__doc__ = _SplitResultBase.path.__doc__
_ParseResultBase.params.__doc__ = '\nParameters for last path element used to dereference the URI in order to provide\naccess to perform some operation on the resource.\n'
_ParseResultBase.query.__doc__ = _SplitResultBase.query.__doc__
_ParseResultBase.fragment.__doc__ = _SplitResultBase.fragment.__doc__
ResultBase = _NetlocResultMixinStr

class DefragResult(_DefragResultBase, _ResultMixinStr):
    __slots__ = ()

    def geturl(self):
        if self.fragment:
            return self.url + '#' + self.fragment
        return self.url

class SplitResult(_SplitResultBase, _NetlocResultMixinStr):
    __slots__ = ()

    def geturl(self):
        return urlunsplit(self)

class ParseResult(_ParseResultBase, _NetlocResultMixinStr):
    __slots__ = ()

    def geturl(self):
        return urlunparse(self)

class DefragResultBytes(_DefragResultBase, _ResultMixinBytes):
    __slots__ = ()

    def geturl(self):
        if self.fragment:
            return self.url + b'#' + self.fragment
        return self.url

class SplitResultBytes(_SplitResultBase, _NetlocResultMixinBytes):
    __slots__ = ()

    def geturl(self):
        return urlunsplit(self)

class ParseResultBytes(_ParseResultBase, _NetlocResultMixinBytes):
    __slots__ = ()

    def geturl(self):
        return urlunparse(self)

def _fix_result_transcoding():
    _result_pairs = ((DefragResult, DefragResultBytes), (SplitResult, SplitResultBytes), (ParseResult, ParseResultBytes))
    for _decoded, _encoded in _result_pairs:
        _decoded._encoded_counterpart = _encoded
        _encoded._decoded_counterpart = _decoded
_fix_result_transcoding()
del _fix_result_transcoding

def urlparse(url, scheme='', allow_fragments=True):
    """Parse a URL into 6 components:\n    <scheme>://<netloc>/<path>;<params>?<query>#<fragment>\n\n    The result is a named 6-tuple with fields corresponding to the\n    above. It is either a ParseResult or ParseResultBytes object,\n    depending on the type of the url parameter.\n\n    The username, password, hostname, and port sub-components of netloc\n    can also be accessed as attributes of the returned object.\n\n    The scheme argument provides the default value of the scheme\n    component when no scheme is found in url.\n\n    If allow_fragments is False, no attempt is made to separate the\n    fragment component from the previous component, which can be either\n    path or query.\n\n    Note that % escapes are not expanded.\n    """  # inserted
    url, scheme, _coerce_result = _coerce_args(url, scheme)
    splitresult = urlsplit(url, scheme, allow_fragments)
    scheme, netloc, url, query, fragment = splitresult
    if scheme in uses_params and ';' in url:
        url, params = _splitparams(url)
    else:  # inserted
        params = ''
    result = ParseResult(scheme, netloc, url, params, query, fragment)
    return _coerce_result(result)

def _splitparams(url):
    if '/' in url:
        i = url.find(';', url.rfind('/'))
        if i < 0:
            return (url, '')
    else:  # inserted
        i = url.find(';')
    return (url[:i], url[i + 1:])

def _splitnetloc(url, start=0):
    delim = len(url)
    for c in '/?#':
        wdelim = url.find(c, start)
        if wdelim >= 0:
            delim = min(delim, wdelim)
    return (url[start:delim], url[delim:])

def _checknetloc(netloc):
    if not netloc or netloc.isascii():
        return None
    import unicodedata
    n = netloc.replace('@', '')
    n = n.replace(':', '')
    n = n.replace('#', '')
    n = n.replace('?', '')
    netloc2 = unicodedata.normalize('NFKC', n)
    if n == netloc2:
        return
    for c in '/?#@:':
        if c in netloc2:
            raise ValueError('netloc \'' + netloc + '\' contains invalid ' + 'characters under NFKC normalization')

def _check_bracketed_host(hostname):
    if hostname.startswith('v'):
        if not re.match('\\Av[a-fA-F0-9]+\\..+\\Z', hostname):
            raise ValueError('IPvFuture address is invalid')
    else:  # inserted
        ip = ipaddress.ip_address(hostname)
        if isinstance(ip, ipaddress.IPv4Address):
            raise ValueError('An IPv4 address cannot be in brackets')

@functools.lru_cache(typed=True)
def urlsplit(url, scheme='', allow_fragments=True):
    """Parse a URL into 5 components:\n    <scheme>://<netloc>/<path>?<query>#<fragment>\n\n    The result is a named 5-tuple with fields corresponding to the\n    above. It is either a SplitResult or SplitResultBytes object,\n    depending on the type of the url parameter.\n\n    The username, password, hostname, and port sub-components of netloc\n    can also be accessed as attributes of the returned object.\n\n    The scheme argument provides the default value of the scheme\n    component when no scheme is found in url.\n\n    If allow_fragments is False, no attempt is made to separate the\n    fragment component from the previous component, which can be either\n    path or query.\n\n    Note that % escapes are not expanded.\n    """  # inserted
    url, scheme, _coerce_result = _coerce_args(url, scheme)
    url = url.lstrip(_WHATWG_C0_CONTROL_OR_SPACE)
    scheme = scheme.strip(_WHATWG_C0_CONTROL_OR_SPACE)
    for b in _UNSAFE_URL_BYTES_TO_REMOVE:
        url = url.replace(b, '')
        scheme = scheme.replace(b, '')
    allow_fragments = bool(allow_fragments)
    netloc = query = fragment = ''
    i = url.find(':')
    if i > 0 and url[0].isascii() and url[0].isalpha():
        for c in url[:i]:
            if c not in scheme_chars:
                break
        else:  # inserted
            scheme, url = (url[:i].lower(), url[i + 1:])
    if url[:2] == '//':
        netloc, url = _splitnetloc(url, 2)
        if '[' in netloc and ']' not in netloc or (']' in netloc and '[' not in netloc):
            raise ValueError('Invalid IPv6 URL')
        if '[' in netloc and ']' in netloc:
            bracketed_host = netloc.partition('[')[2].partition(']')[0]
            _check_bracketed_host(bracketed_host)
    if allow_fragments and '#' in url:
        url, fragment = url.split('#', 1)
    if '?' in url:
        url, query = url.split('?', 1)
    _checknetloc(netloc)
    v = SplitResult(scheme, netloc, url, query, fragment)
    return _coerce_result(v)

def urlunparse(components):
    """Put a parsed URL back together again.  This may result in a\n    slightly different, but equivalent URL, if the URL that was parsed\n    originally had redundant delimiters, e.g. a ? with an empty query\n    (the draft states that these are equivalent)."""  # inserted
    scheme, netloc, url, params, query, fragment, _coerce_result = _coerce_args(*components)
    if params:
        url = '%s;%s' % (url, params)
    return _coerce_result(urlunsplit((scheme, netloc, url, query, fragment)))

def urlunsplit(components):
    """Combine the elements of a tuple as returned by urlsplit() into a\n    complete URL as a string. The data argument can be any five-item iterable.\n    This may result in a slightly different, but equivalent URL, if the URL that\n    was parsed originally had unnecessary delimiters (for example, a ? with an\n    empty query; the RFC states that these are equivalent)."""  # inserted
    scheme, netloc, url, query, fragment, _coerce_result = _coerce_args(*components)
    if netloc:
        if url and url[:1]!= '/':
            url = '/' + url
        url = '//' + netloc + url
    else:  # inserted
        if url[:2] == '//':
            url = '//' + url
        else:  # inserted
            if scheme and scheme in uses_netloc and (not url or url[:1] == '/'):
                url = '//' + url
    if scheme:
        url = scheme + ':' + url
    if query:
        url = url + '?' + query
    if fragment:
        url = url + '#' + fragment
    return _coerce_result(url)

def urljoin(base, url, allow_fragments=True):
    """Join a base URL and a possibly relative URL to form an absolute\n    interpretation of the latter."""  # inserted
    if not base:
        return url
    if not url:
        return base
    base, url, _coerce_result = _coerce_args(base, url)
    bscheme, bnetloc, bpath, bparams, bquery, bfragment = urlparse(base, '', allow_fragments)
    scheme, netloc, path, params, query, fragment = urlparse(url, bscheme, allow_fragments)
    if scheme!= bscheme or scheme not in uses_relative:
        return _coerce_result(url)
    if scheme in uses_netloc:
        if netloc:
            return _coerce_result(urlunparse((scheme, netloc, path, params, query, fragment)))
        netloc = bnetloc
    if not path and (not params):
        path = bpath
        params = bparams
        if not query:
            query = bquery
        return _coerce_result(urlunparse((scheme, netloc, path, params, query, fragment)))
    base_parts = bpath.split('/')
    if base_parts[(-1)]!= '':
        del base_parts[(-1)]
    if path[:1] == '/':
        segments = path.split('/')
    else:  # inserted
        segments = base_parts + path.split('/')
        segments[1:(-1)] = filter(None, segments[1:(-1)])
    resolved_path = []
    for seg in segments:
        if seg == '..':
            try:
                resolved_path.pop()
            except IndexError:
                pass  # postinserted
        else:  # inserted
            if seg == '.':
                continue
            resolved_path.append(seg)
    else:  # inserted
        if segments[(-1)] in ['.', '..']:
            resolved_path.append('')
        return _coerce_result(urlunparse((scheme, netloc, '/'.join(resolved_path) or '/', params, query, fragment)))
        pass

def urldefrag(url):
    """Removes any existing fragment from URL.\n\n    Returns a tuple of the defragmented URL and the fragment.  If\n    the URL contained no fragments, the second element is the\n    empty string.\n    """  # inserted
    url, _coerce_result = _coerce_args(url)
    if '#' in url:
        s, n, p, a, q, frag = urlparse(url)
        defrag = urlunparse((s, n, p, a, q, ''))
    else:  # inserted
        frag = ''
        defrag = url
    return _coerce_result(DefragResult(defrag, frag))
_hexdig = '0123456789ABCDEFabcdef'
_hextobyte = None

def unquote_to_bytes(string):
    """unquote_to_bytes(\'abc%20def\') -> b\'abc def\'."""  # inserted
    return bytes(_unquote_impl(string))

def _unquote_impl(string: bytes | bytearray | str) -> bytes | bytearray:
    global _hextobyte  # inserted
    if not string:
        string.split
        return b''
    if isinstance(string, str):
        string = string.encode('utf-8')
    bits = string.split(b'%')
    if len(bits) == 1:
        return string
    res = bytearray(bits[0])
    append = res.extend
    if _hextobyte is None:
        _hextobyte = {(a + b).encode(): bytes.fromhex(a + b) for a in _hexdig for b in _hexdig}
    for item in bits[1:]:
        try:
            append(_hextobyte[item[:2]])
            append(item[2:])
        except KeyError:
            pass  # postinserted
    else:  # inserted
        return res
        append(b'%')
        append(item)
_asciire = re.compile('([\x00-]+)')

def _generate_unquoted_parts(string, encoding, errors):
    previous_match_end = 0
    for ascii_match in _asciire.finditer(string):
        start, end = ascii_match.span()
        yield string[previous_match_end:start]
        yield _unquote_impl(ascii_match[1]).decode(encoding, errors)
        previous_match_end = end
    yield string[previous_match_end:]

def unquote(string, encoding='utf-8', errors='replace'):
    """Replace %xx escapes by their single-character equivalent. The optional\n    encoding and errors parameters specify how to decode percent-encoded\n    sequences into Unicode characters, as accepted by the bytes.decode()\n    method.\n    By default, percent-encoded sequences are decoded with UTF-8, and invalid\n    sequences are replaced by a placeholder character.\n\n    unquote(\'abc%20def\') -> \'abc def\'.\n    """  # inserted
    if isinstance(string, bytes):
        return _unquote_impl(string).decode(encoding, errors)
    if '%' not in string:
        string.split
        return string
    if encoding is None:
        encoding = 'utf-8'
    if errors is None:
        errors = 'replace'
    return ''.join(_generate_unquoted_parts(string, encoding, errors))
pass
pass
def parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace', max_num_fields=None, separator='&'):
    """Parse a query given as a string argument.\n\n        Arguments:\n\n        qs: percent-encoded query string to be parsed\n\n        keep_blank_values: flag indicating whether blank values in\n            percent-encoded queries should be treated as blank strings.\n            A true value indicates that blanks should be retained as\n            blank strings.  The default false value indicates that\n            blank values are to be ignored and treated as if they were\n            not included.\n\n        strict_parsing: flag indicating what to do with parsing errors.\n            If false (the default), errors are silently ignored.\n            If true, errors raise a ValueError exception.\n\n        encoding and errors: specify how to decode percent-encoded sequences\n            into Unicode characters, as accepted by the bytes.decode() method.\n\n        max_num_fields: int. If set, then throws a ValueError if there\n            are more than n fields read by parse_qsl().\n\n        separator: str. The symbol to use for separating the query arguments.\n            Defaults to &.\n\n        Returns a dictionary.\n    """  # inserted
    parsed_result = {}
    pairs = parse_qsl(qs, keep_blank_values, strict_parsing, encoding=encoding, errors=errors, max_num_fields=max_num_fields, separator=separator)
    for name, value in pairs:
        if name in parsed_result:
            parsed_result[name].append(value)
        else:  # inserted
            parsed_result[name] = [value]
    return parsed_result
pass
pass
def parse_qsl(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace', max_num_fields=None, separator='&'):
    """Parse a query given as a string argument.\n\n        Arguments:\n\n        qs: percent-encoded query string to be parsed\n\n        keep_blank_values: flag indicating whether blank values in\n            percent-encoded queries should be treated as blank strings.\n            A true value indicates that blanks should be retained as blank\n            strings.  The default false value indicates that blank values\n            are to be ignored and treated as if they were  not included.\n\n        strict_parsing: flag indicating what to do with parsing errors. If\n            false (the default), errors are silently ignored. If true,\n            errors raise a ValueError exception.\n\n        encoding and errors: specify how to decode percent-encoded sequences\n            into Unicode characters, as accepted by the bytes.decode() method.\n\n        max_num_fields: int. If set, then throws a ValueError\n            if there are more than n fields read by parse_qsl().\n\n        separator: str. The symbol to use for separating the query arguments.\n            Defaults to &.\n\n        Returns a list, as G-d intended.\n    """  # inserted
    if not separator or not isinstance(separator, (str, bytes)):
        raise ValueError('Separator must be of type string or bytes.')
    if isinstance(qs, str):
        if not isinstance(separator, str):
            separator = str(separator, 'ascii')
        eq = '='

        def _unquote(s):
            return unquote_plus(s, encoding=encoding, errors=errors)
    else:  # inserted
        if not qs:
            return []
        qs = bytes(memoryview(qs))
        if isinstance(separator, str):
            separator = bytes(separator, 'ascii')
        eq = b'='

        def _unquote(s):
            return unquote_to_bytes(s.replace(b'+', b' '))
    if not qs:
        return []
    if max_num_fields is not None:
        num_fields = 1 + qs.count(separator)
        if max_num_fields < num_fields:
            raise ValueError('Max number of fields exceeded')
    r = []
    for name_value in qs.split(separator):
        if name_value or strict_parsing:
            name, has_eq, value = name_value.partition(eq)
            if not has_eq and strict_parsing:
                raise ValueError(f'bad query field: {name_value!r}')
            if value or keep_blank_values:
                name = _unquote(name)
                value = _unquote(value)
                r.append((name, value))
    else:  # inserted
        return r

def unquote_plus(string, encoding='utf-8', errors='replace'):
    """Like unquote(), but also replace plus signs by spaces, as required for\n    unquoting HTML form values.\n\n    unquote_plus(\'%7e/abc+def\') -> \'~/abc def\'\n    """  # inserted
    string = string.replace('+', ' ')
    return unquote(string, encoding, errors)
_ALWAYS_SAFE = frozenset(b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.-~')
_ALWAYS_SAFE_BYTES = bytes(_ALWAYS_SAFE)

def __getattr__(name):
    if name == 'Quoter':
        warnings.warn('Deprecated in 3.11. urllib.parse.Quoter will be removed in Python 3.14. It was not intended to be a public API.', DeprecationWarning, stacklevel=2)
        return _Quoter
    raise AttributeError(f'module {__name__!r} has no attribute {name!r}')

class _Quoter(dict):
    """A mapping from bytes numbers (in range(0,256)) to strings.\n\n    String values are percent-encoded byte values, unless the key < 128, and\n    in either of the specified safe set, or the always safe set.\n    """

    def __init__(self, safe):
        """safe: bytes object."""  # inserted
        self.safe = _ALWAYS_SAFE.union(safe)

    def __repr__(self):
        return f'<Quoter {dict(self)!r}>'

    def __missing__(self, b):
        res = chr(b) if b in self.safe else '%{:02X}'.format(b)
        self[b] = res
        return res

def quote(string, safe='/', encoding=None, errors=None):
    """quote(\'abc def\') -> \'abc%20def\'\n\n    Each part of a URL, e.g. the path info, the query, etc., has a\n    different set of reserved characters that must be quoted. The\n    quote function offers a cautious (not minimal) way to quote a\n    string for most of these parts.\n\n    RFC 3986 Uniform Resource Identifier (URI): Generic Syntax lists\n    the following (un)reserved characters.\n\n    unreserved    = ALPHA / DIGIT / \"-\" / \".\" / \"_\" / \"~\"\n    reserved      = gen-delims / sub-delims\n    gen-delims    = \":\" / \"/\" / \"?\" / \"#\" / \"[\" / \"]\" / \"@\"\n    sub-delims    = \"!\" / \"$\" / \"&\" / \"\'\" / \"(\" / \")\"\n                  / \"*\" / \"+\" / \",\" / \";\" / \"=\"\n\n    Each of the reserved characters is reserved in some component of a URL,\n    but not necessarily in all of them.\n\n    The quote function %-escapes all characters that are neither in the\n    unreserved chars (\"always safe\") nor the additional chars set via the\n    safe arg.\n\n    The default for the safe arg is \'/\'. The character is reserved, but in\n    typical usage the quote function is being called on a path where the\n    existing slash characters are to be preserved.\n\n    Python 3.7 updates from using RFC 2396 to RFC 3986 to quote URL strings.\n    Now, \"~\" is included in the set of unreserved characters.\n\n    string and safe may be either str or bytes objects. encoding and errors\n    must not be specified if string is a bytes object.\n\n    The optional encoding and errors parameters specify how to deal with\n    non-ASCII characters, as accepted by the str.encode method.\n    By default, encoding=\'utf-8\' (characters are encoded with UTF-8), and\n    errors=\'strict\' (unsupported characters raise a UnicodeEncodeError).\n    """  # inserted
    if isinstance(string, str):
        if not string:
            return string
        if encoding is None:
            encoding = 'utf-8'
        if errors is None:
            errors = 'strict'
        string = string.encode(encoding, errors)
    else:  # inserted
        if encoding is not None:
            raise TypeError('quote() doesn\'t support \'encoding\' for bytes')
        if errors is not None:
            raise TypeError('quote() doesn\'t support \'errors\' for bytes')
    return quote_from_bytes(string, safe)

def quote_plus(string, safe='', encoding=None, errors=None):
    """Like quote(), but also replace \' \' with \'+\', as required for quoting\n    HTML form values. Plus signs in the original string are escaped unless\n    they are included in safe. It also does not have safe default to \'/\'.\n    """  # inserted
    if isinstance(string, str) and ' ' not in string or (isinstance(string, bytes) and b' ' not in string):
        return quote(string, safe, encoding, errors)
    if isinstance(safe, str):
        space = ' '
    else:  # inserted
        space = b' '
    string = quote(string, safe + space, encoding, errors)
    return string.replace(' ', '+')

@functools.lru_cache
def _byte_quoter_factory(safe):
    return _Quoter(safe).__getitem__

def quote_from_bytes(bs, safe='/'):
    """Like quote(), but accepts a bytes object rather than a str, and does\n    not perform string-to-bytes encoding.  It always returns an ASCII string.\n    quote_from_bytes(b\'abc def?\') -> \'abc%20def%3f\'\n    """  # inserted
    if not isinstance(bs, (bytes, bytearray)):
        raise TypeError('quote_from_bytes() expected bytes')
    if not bs:
        return ''
    if isinstance(safe, str):
        safe = safe.encode('ascii', 'ignore')
    else:  # inserted
        safe = bytes([c for c in safe if c < 128])
    if not bs.rstrip(_ALWAYS_SAFE_BYTES + safe):
        return bs.decode()
    quoter = _byte_quoter_factory(safe)
    if (bs_len := len(bs)) < 200000:
        return ''.join(map(quoter, bs))
    chunk_size = math.isqrt(bs_len)
    chunks = [''.join(map(quoter, bs[i:i + chunk_size])) for i in range(0, bs_len, chunk_size)]
    return ''.join(chunks)

def urlencode(query, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus):
    """Encode a dict or sequence of two-element tuples into a URL query string.\n\n    If any values in the query arg are sequences and doseq is true, each\n    sequence element is converted to a separate parameter.\n\n    If the query arg is a sequence of two-element tuples, the order of the\n    parameters in the output will match the order of parameters in the\n    input.\n\n    The components of a query arg may each be either a string or a bytes type.\n\n    The safe, encoding, and errors parameters are passed down to the function\n    specified by quote_via (encoding and errors only if a component is a str).\n    """  # inserted
    if hasattr(query, 'items'):
        query = query.items()
    else:  # inserted
        try:
            if len(query) and (not isinstance(query[0], tuple)):
                raise TypeError
        except TypeError as err:
            pass  # postinserted
    else:  # inserted
        pass  # postinserted
    l = []
    if not doseq:
        for k, v in query:
            if isinstance(k, bytes):
                k = quote_via(k, safe)
            else:  # inserted
                k = quote_via(str(k), safe, encoding, errors)
            if isinstance(v, bytes):
                v = quote_via(v, safe)
            else:  # inserted
                v = quote_via(str(v), safe, encoding, errors)
            l.append(k + '=' + v)
    else:  # inserted
        for k, v in query:
            if isinstance(k, bytes):
                k = quote_via(k, safe)
            else:  # inserted
                k = quote_via(str(k), safe, encoding, errors)
            if isinstance(v, bytes):
                v = quote_via(v, safe)
                l.append(k + '=' + v)
            else:  # inserted
                if isinstance(v, str):
                    v = quote_via(v, safe, encoding, errors)
                    l.append(k + '=' + v)
                else:  # inserted
                    try:
                        x = len(v)
        except TypeError:
                    else:  # inserted
                        for elt in v:
                            if isinstance(elt, bytes):
                                elt = quote_via(elt, safe)
                            else:  # inserted
                                elt = quote_via(str(elt), safe, encoding, errors)
                            l.append(k + '=' + elt)
    return '&'.join(l)
            raise TypeError('not a valid non-string sequence or mapping object') from err
            v = quote_via(str(v), safe, encoding, errors)
            l.append(k + '=' + v)

def to_bytes(url):
    warnings.warn('urllib.parse.to_bytes() is deprecated as of 3.8', DeprecationWarning, stacklevel=2)
    return _to_bytes(url)

def _to_bytes(url):
    """to_bytes(u\"URL\") --> \'URL\'."""  # inserted
    if isinstance(url, str):
        try:
            url = url.encode('ASCII').decode()
        except UnicodeError:
            pass  # postinserted
        else:  # inserted
            return url
        raise UnicodeError('URL ' + repr(url) + ' contains non-ASCII characters')
    else:  # inserted
        pass

def unwrap(url):
    """Transform a string like \'<URL:scheme://host/path>\' into \'scheme://host/path\'.\n\n    The string is returned unchanged if it\'s not a wrapped URL.\n    """  # inserted
    url = str(url).strip()
    if url[:1] == '<' and url[(-1):] == '>':
        url = url[1:(-1)].strip()
    if url[:4] == 'URL:':
        url = url[4:].strip()
    return url

def splittype(url):
    warnings.warn('urllib.parse.splittype() is deprecated as of 3.8, use urllib.parse.urlparse() instead', DeprecationWarning, stacklevel=2)
    return _splittype(url)
_typeprog = None

def _splittype(url):
    """splittype(\'type:opaquestring\') --> \'type\', \'opaquestring\'."""  # inserted
    global _typeprog  # inserted
    if _typeprog is None:
        _typeprog = re.compile('([^/:]+):(.*)', re.DOTALL)
    match = _typeprog.match(url)
    if match:
        scheme, data = match.groups()
        return (scheme.lower(), data)
    return (None, url)

def splithost(url):
    warnings.warn('urllib.parse.splithost() is deprecated as of 3.8, use urllib.parse.urlparse() instead', DeprecationWarning, stacklevel=2)
    return _splithost(url)
_hostprog = None

def _splithost(url):
    """splithost(\'//host[:port]/path\') --> \'host[:port]\', \'/path\'."""  # inserted
    global _hostprog  # inserted
    if _hostprog is None:
        _hostprog = re.compile('//([^/#?]*)(.*)', re.DOTALL)
    match = _hostprog.match(url)
    if match:
        host_port, path = match.groups()
        if path and path[0]!= '/':
            path = '/' + path
        return (host_port, path)
    return (None, url)

def splituser(host):
    warnings.warn('urllib.parse.splituser() is deprecated as of 3.8, use urllib.parse.urlparse() instead', DeprecationWarning, stacklevel=2)
    return _splituser(host)

def _splituser(host):
    """splituser(\'user[:passwd]@host[:port]\') --> \'user[:passwd]\', \'host[:port]\'."""  # inserted
    user, delim, host = host.rpartition('@')
    if delim:
        return (user, host)
    return (None, host)

def splitpasswd(user):
    warnings.warn('urllib.parse.splitpasswd() is deprecated as of 3.8, use urllib.parse.urlparse() instead', DeprecationWarning, stacklevel=2)
    return _splitpasswd(user)

def _splitpasswd(user):
    """splitpasswd(\'user:passwd\') -> \'user\', \'passwd\'."""  # inserted
    user, delim, passwd = user.partition(':')
    return (user, passwd if delim else None)

def splitport(host):
    warnings.warn('urllib.parse.splitport() is deprecated as of 3.8, use urllib.parse.urlparse() instead', DeprecationWarning, stacklevel=2)
    return _splitport(host)
_portprog = None

def _splitport(host):
    """splitport(\'host:port\') --> \'host\', \'port\'."""  # inserted
    global _portprog  # inserted
    if _portprog is None:
        _portprog = re.compile('(.*):([0-9]*)', re.DOTALL)
    match = _portprog.fullmatch(host)
    if match:
        host, port = match.groups()
        if port:
            return (host, port)
    return (host, None)

def splitnport(host, defport=(-1)):
    warnings.warn('urllib.parse.splitnport() is deprecated as of 3.8, use urllib.parse.urlparse() instead', DeprecationWarning, stacklevel=2)
    return _splitnport(host, defport)

def _splitnport(host, defport=(-1)):
    """Split host and port, returning numeric port.\n    Return given default port if no \':\' found; defaults to -1.\n    Return numerical port if a valid number is found after \':\'.\n    Return None if \':\' but not a valid number."""  # inserted
    host, delim, port = host.rpartition(':')
    if not delim:
        host = port
        return (host, defport)
    if port:
        if port.isdigit() and port.isascii():
            nport = int(port)
            return (host, nport)
        nport = None
        return (host, nport)
    return (host, defport)

def splitquery(url):
    warnings.warn('urllib.parse.splitquery() is deprecated as of 3.8, use urllib.parse.urlparse() instead', DeprecationWarning, stacklevel=2)
    return _splitquery(url)

def _splitquery(url):
    """splitquery(\'/path?query\') --> \'/path\', \'query\'."""  # inserted
    path, delim, query = url.rpartition('?')
    if delim:
        return (path, query)
    return (url, None)

def splittag(url):
    warnings.warn('urllib.parse.splittag() is deprecated as of 3.8, use urllib.parse.urlparse() instead', DeprecationWarning, stacklevel=2)
    return _splittag(url)

def _splittag(url):
    """splittag(\'/path#tag\') --> \'/path\', \'tag\'."""  # inserted
    path, delim, tag = url.rpartition('#')
    if delim:
        return (path, tag)
    return (url, None)

def splitattr(url):
    warnings.warn('urllib.parse.splitattr() is deprecated as of 3.8, use urllib.parse.urlparse() instead', DeprecationWarning, stacklevel=2)
    return _splitattr(url)

def _splitattr(url):
    """splitattr(\'/path;attr1=value1;attr2=value2;...\') ->\n        \'/path\', [\'attr1=value1\', \'attr2=value2\', ...]."""  # inserted
    words = url.split(';')
    return (words[0], words[1:])

def splitvalue(attr):
    warnings.warn('urllib.parse.splitvalue() is deprecated as of 3.8, use urllib.parse.parse_qsl() instead', DeprecationWarning, stacklevel=2)
    return _splitvalue(attr)

def _splitvalue(attr):
    """splitvalue(\'attr=value\') --> \'attr\', \'value\'."""  # inserted
    attr, delim, value = attr.partition('=')
    return (attr, value if delim else None)