""" Python module which holds custom field value validators """


def dp_field_value_validator(record):
    return record["dp"] in [1, 2, 3]