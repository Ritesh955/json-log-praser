""" Python module which holds custom field value validators """
import re


def dp_field_value_validator(record):
    """
    function to ensure dp field value is amongst 1,2,3
    :param record: json log line
    :return: boolean true or false
    """
    return record["dp"] in [1, 2, 3]


def nm_field_value_validator(record):
    """
    function to validate file name using regex.
    :param record: json log line
    :return: none if invalid filename
    """
    file_name = record["nm"]
    pattern = re.compile("^[\w,\s-]+\.[A-Za-z]{3,4}$")
    return pattern.match(file_name)

