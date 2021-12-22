from jsonschema import validate, exceptions
from config import JSON_LOG_RECORD_SCHEMA
from log_parser import field_validators


def process_json_log(sample_json_log):
    """
    function to validate json record and dp field_value
    and return a map of unique file extension and distinct file names
    """

    file_ext_to_name = {}

    for log_line in sample_json_log:
        try:
            if validate(log_line, schema=JSON_LOG_RECORD_SCHEMA) is None:
                if field_validators.dp_field_value_validator(log_line):
                    file_name, ext = log_line["nm"].strip().split(".")
                    if ext in file_ext_to_name:
                        file_ext_to_name[ext].add(file_name)
                    else:
                        file_ext_to_name[ext] = set([file_name])
        except exceptions.ValidationError as e:
            pass

    return file_ext_to_name


def get_file_ext_to_file_name_count(file_ext_to_name):
    """
    function to covert a map of unique file extension and distinct file names into
    file extensions and file counts
    """
    file_ext_to_name_count = {}
    for key in file_ext_to_name:
        file_ext_to_name_count[key] = len(file_ext_to_name[key])
    return file_ext_to_name_count

