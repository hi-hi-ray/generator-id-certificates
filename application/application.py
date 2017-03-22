# -*- coding: utf-8 -*-

import string
import random
import json

# Constant
__JSON_PATH = 'informations.json'

# Dict
_data = []

def generator-id():
    return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase
    + string.digits) for i in range(data['quantity_of_characters']))

def get-informations(path_file):
    with open(path_file) as json_data:
        _data = json.load(json_data)
