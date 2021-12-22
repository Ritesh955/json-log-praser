from jsonschema import validate, exceptions
from log_parser import field_validators
import config


def process_json_log(sample_json_log):
    """
    function to validate json record and dp field_value
    and return a map of unique file extension and distinct file names
    :param record: smaple json log
    :return: file extension to file name map/dict
    """

    file_ext_to_name = {}

    for log_line in sample_json_log:
        try:
            if (
                validate(log_line, schema=config.JSON_LOG_RECORD_SCHEMA) is None
                and len(log_line.keys()) == config.JSON_LOG_RECORD_FIELD_COUNT
            ):
                if (
                    field_validators.dp_field_value_validator(log_line)
                    and field_validators.nm_field_value_validator(log_line)
                ):
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
    :param record: file extension to file name map/dict
    :return: file extension to file count map/dict
    """
    file_ext_to_name_count = {}
    for key in file_ext_to_name:
        file_ext_to_name_count[key] = len(file_ext_to_name[key])
    return file_ext_to_name_count

