import os


def joinpath(*args):
    return os.path.join(*args)


# DONE: Resolve paths
ROOT = os.path.dirname(__file__)
# SUBFOLDER NAME  = joinpath(ROOT, 'subfolder name')
