import subprocess
import logging
import os

log = logging.getLogger(__name__)

def funnyFunc():
  log.error('Oh noes')


def run_command(
        command,
        split=False,
        ignore_error=False,
        include_errors=True):
    """
    Execute subprocesses.
    """
    log.debug('Running %s', ' '.join(command))

    env = os.environ.copy()

    if include_errors:
        error_pipe = subprocess.STDOUT
    else:
        error_pipe = subprocess.PIPE

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

def do_thing():
    print 'thinger'
    print 'thing 2'
