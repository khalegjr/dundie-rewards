"""Core module of dundie"""
from dundie.utils.log import get_logger

log = get_logger()


def load(filepath):
    """
    Loads data from filepath to the database

    >>> len(load('assets/people.csv'))
    2

    >>> load('assets/people.csv')[0][0]
    'J'
    """
    try:
        with open(filepath) as file_:
            return [line.strip() for line in file_.readlines()]
    except FileNotFoundError as e:
        log.error(str(e))
        raise e
