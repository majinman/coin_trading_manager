import json
from flask_sqlalchemy import DeclarativeMeta
from sqlalchemy_utils.types.choice import Choice
import numpy as np
import time
import random
import string
from datetime import datetime
from decimal import Decimal
import decimal
import arrow
# from bson import json_util
import datetime as dt
from collections import OrderedDict
from collections import Counter
import jwt
import uuid
import hashlib
from urllib.parse import urlencode


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super(DatetimeEncoder, obj).default(obj)
        except TypeError:
            return str(obj)


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj)
                          if not x.startswith('_') and not x.endswith('_') and x != 'metadata' and not x[0].istitle() and
                          not x.startswith('query')]:
                data = obj.__getattribute__(field)
                try:
                    # print("{} {}".format(field, type(data)))
                    if type(data) == Choice:
                        data = data.value
                    elif type(data) == datetime:
                        data = data.strftime('%Y-%m-%d %H:%M:%S')
                    elif type(data) == Decimal:
                        data = float(data)
                    else:
                        json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        elif isinstance(obj, decimal.Decimal):
            return json.dumps(obj, cls=DecimalEncoder)
        elif isinstance(obj, datetime):
            # return json.dumps(obj, cls=DatetimeEncoder)
            return obj.isoformat()
            # return obj.strftime('%Y-%m-%d')

        # raise TypeError('not JSON serializable')

        return json.JSONEncoder.default(self, obj)


def serialize_query(query_object):
    return json.loads(json.dumps(query_object, cls=AlchemyEncoder))

#
# class SmartDict(dict):
#     def __init__(self):
#         self = dict()
#
#     def add(self, key, value):
#         self[key] = value
#
# def get_type(value):
#     if isinstance(value, dict):
#         return {key: get_type(value[key]) for key in value}
#     else:
#         return type(value)
#
#
# def dict_type_validation(required_type, data):
#     input_type = get_type(data)
#     if len(required_type) != len(data):
#         return False
#
#     if input_type != required_type:
#         return False
#     return True
#
#
# def get_random_string(stringLength=10):
#     """Generate a random string of fixed length """
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for i in range(stringLength))
#
def get_datetime_from_string(date_str, delimiter):
    date = arrow.get(date_str, 'YYYY{delimiter}MM{delimiter}DD'.format(delimiter=delimiter)).datetime
    return date

def get_datetime_from_string_no_delimiter(date_str):
    date = arrow.get(date_str, 'YYMMDD').datetime
    return date


def get_datetime_today_with_no_time(input_datetime=None):
    if input_datetime:
        input_datetime = input_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
        return input_datetime

    else:
        a = arrow.utcnow().shift(hours=+9).replace(hour=0, minute=0, second=0, microsecond=0)
        return a.datetime

def get_current_datetime():
    return arrow.utcnow().shift(hours=9).datetime


def get_sec_difference_between_datetime(time1, time2):
    print("time: ", (time2 - time1).seconds)
    return (time2 - time1).seconds


def get_simple_date(input_datetime=None):
    input_datetime = input_datetime.replace(hour=0, minute=0, second=0, microsecond=0) if input_datetime else arrow.utcnow().shift(hours=+9)

    return '{}-{}-{}'.format(input_datetime.year, input_datetime.month, input_datetime.day)

class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)


class UPBitUtils():
    def get_uuid(self):
        return str(uuid.uuid4())

    def get_jwt_token(self, payload, secret_key):
        return jwt.encode(payload, secret_key)

    def get_query_hash(self, query_string):
        m = hashlib.sha512()
        m.update(query_string)
        return m.hexdigest()

