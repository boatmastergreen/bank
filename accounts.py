#!/usr/bin/env python3

from collections import namedtuple
import flask
from functools import partial
from jinja2 import Template
import json
from random import randint


def first(iterable):
    return next(iter(iterable))


def new_id(digits=8, ids=None):
    old_ids = [] if ids is None else ids
    nums = iter(partial(randint, 10**digits, 10**(digits+1)),
                None)
    return first(num for num in nums if num not in ids)

name = namedtuple('name', 'first, last')

class Account:
    def __init__(self, name, pin, password):
        if isinstance(name, w):
            pass

    @classmethod
    def from_dict(cls, d):
        '''Factory method for converting dicts
        to accounts. Useful for talking to JSON.'''
        return cls(**d)

    def to_dict(self):
        '''Convert to dict'''
        
