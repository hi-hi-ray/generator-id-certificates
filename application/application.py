# -*- coding: utf-8 -*-

import os
import string
import random
import json

# Constant
__JSON_FILE_NAME = 'informations.json'

# Dict
_data = {}

def generator_id(quantity_of_characters, organization_abbreviation):
    id = ''.join(random.choice(string.ascii_lowercase +
    string.ascii_uppercase + string.digits) for i in range(quantity_of_characters))
    return organization_abbreviation + "-" + id


def get_informations(path_file):
    with open(path_file) as json_data:
        data = json.load(json_data)
    return data

def get_relative_path():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, __JSON_FILE_NAME)
    return filename


def create_file_with_ids():
    print('Getting Configurations')
    _data = get_informations(get_relative_path())

    print('Creating a cool name for your file')
    name = _data['organization_name'] + '_' + _data['event_name']
    name_file = _data['path_to_save_file'] + name +'.txt'

    print('Creating new text file')
    with open(name_file, 'a') as txt_file:
        for i in range(_data['quantity_of_certificates']):
            txt_file.writelines(generator_id(_data['quantity_of_characters'],
            _data['organization_abbreviation']) + '\n')

create_file_with_ids()