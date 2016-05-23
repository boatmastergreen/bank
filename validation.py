#!/usr/bin/env python3

from functools import singledispatch
from hashlib import md5
import json


'''
example:
{"name": {"first": "Edward",
          "last": "Minnix"},
 "pin": "b'?\\xa1F!\\x9cH\\xa49:\\xac\\xe2>\\x8f51%'"
 "user_id": 439750760
}
'''

@singledispatch
def validate_pin(pin):
    raise TypeError

@validate_pin.register(int)
def _(pin):
    pass

@validate_pin.register(str)
def _(pin):
    pass
