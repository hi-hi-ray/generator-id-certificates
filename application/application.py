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
    print('Getting Configurations')
    with open(path_file) as json_data:
        data = json.load(json_data)
    return data

def get_relative_path():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, __JSON_FILE_NAME)
    return filename

def verify_the_fields(**_data):
    print('Checking if there is nothing empty')
    if _data['organization_name'] == "":
        raise Exception('Oh! Thats bad, You need to fill the organization_name field.')
    if  isinstance(_data['organization_name'], str) == False:
        raise Exception('Oh! Thats bad, You need to fill the organization_name field with a string type.')
    if _data['event_name'] == "":
        raise Exception('Oh! Thats bad, You need to fill the event_name field.')
    if  isinstance(_data['event_name'], str) == False:
        raise Exception('Oh! Thats bad, You need to fill the event_name field with a string type.')
    if _data['path_to_save_file'] == "":
        raise Exception('Oh! Thats bad, You need to fill the path_to_save_file field.')
    if  isinstance(_data['path_to_save_file'], str) == False:
        raise Exception('Oh! Thats bad, You need to fill the path_to_save_file field with a string type.')
    if _data['organization_abbreviation'] == "":
        raise Exception('Oh! Thats bad, You need to fill the organization_abbreviation field.')
    if  isinstance(_data['organization_abbreviation'], str) == False:
        raise Exception('Oh! Thats bad, You need to fill the organization_abbreviation field with a string type.')
    if _data['quantity_of_certificates'] == "":
        raise Exception('Oh! Thats bad, You need to fill the quantity_of_certificates field.')
    if  isinstance(_data['quantity_of_certificates'], int) == False:
        raise Exception('Oh! Thats bad, You need to fill the quantity_of_certificates field with a int type.')
    if _data['quantity_of_characters'] == "":
        raise Exception('Oh! Thats bad, You need to fill the quantity_of_characters field.')
    if  isinstance(_data['quantity_of_characters'], int) == False:
        raise Exception('Oh! Thats bad, You need to fill the quantity_of_characters field with a int type.')


def create_file_with_ids():
    _data = get_informations(get_relative_path())
    verify_the_fields(**_data)

    print('Creating a cool name for your file')
    name = _data['organization_name'] + '_' + _data['event_name']
    name_file = _data['path_to_save_file'] + name +'.txt'

    print('Creating new text file')
    with open(name_file, 'a') as txt_file:
        for i in range(_data['quantity_of_certificates']):
            txt_file.writelines(generator_id(_data['quantity_of_characters'],
            _data['organization_abbreviation']) + '\n')
    print('Badabim Badabum! Your file was created with success')

create_file_with_ids()