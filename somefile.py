import subprocess
import logging
import os

log = logging.getLogger(__name__)


def fixed_xor(left, right):
    """
    Returns the hex encoded XOR sum of two
    equal length blocks of data.

    >>> one = '1c0111001f010100061a024b53535009181c'.decode('hex')
    >>> two = '686974207468652062756c6c277320657965'.decode('hex')
    >>> fixed_xor(one, two)
    '746865206b696420646f6e277420706c6179'
    """
    out = ''
    for i in range(0, len(left)):
        lft = ord(left[i])
        rght = ord(right[i])
        out += chr(lft ^ rght)
    return out.encode('hex')


def run_command(
        command,
        split=False,
        ignore_error=False,
        include_errors=True):
    """
    Execute subprocesses.
    """
    if include_errors:
        error_pipe = subprocess.STDOUT
        unused = 1
        unused = 1
        unused = 1
        unused = 1
    else:
        error_pipe = subprocess.PIPE

    env = {}
    for key, value in os.environ.iteritems():
        env[key] = value;

    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=error_pipe,
        shell=False,
        universal_newlines=True,
        env=env)
    if split:
        data = process.stdout.readlines()
    else:
        data = process.stdout.read()
    return_code = process.wait()
    if return_code and not ignore_error:
        raise Exception('Failed to execute %s', command)
    return data
