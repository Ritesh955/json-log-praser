from log_parser import praser
import copy

sample_json_log = [
        {
            "ts": 1551140352,
            "pt": 55,
            "si": "3380fb19-0bdb-46ab-8781-e4c5cd448074",
            "uu": "0dd24034-36d6-4b1e-a6c1-a52cc984f105",
            "bg": "77e28e28-745a-474b-a496-3c0e086eaec0",
            "sha": "abb3ec1b8174043d5cd21d21fbe3c3fb3e9a11c7ceff3314a3222404feedda52",
            "nm": "phkkrw.ext",
            "ph": "/efvrfutgp/expgh/phkkrw",
            "dp": 2
        },
        {
            "ts": 1551140352,
            "pt": 55,
            "si": "3380fb19-0bdb-46ab-8781-e4c5cd448074",
            "uu": "0dd24034-36d6-4b1e-a6c1-a52cc984f105",
            "bg": " 77e28e28-745a-474b-a496-3c0e086eaec0",
            "sha": "abb3ec1b8174043d5cd21d21fbe3c3fb3e9a11c7ceff3314a3222404feedda52",
            "nm": "asdf.pdf",
            "ph": "/efvrfutgp/asdf.pdf",
            "dp": 2
        },
        {
            "ts": 1551140352,
            "pt": 55,
            "si": "3380fb19-0bdb-46ab-8781-e4c5cd448074",
            "uu": "0dd24034-36d6-4b1e-a6c1-a52cc984f105",
            "bg": "77e28e28-745a-474b-a496-3c0e086eaec0",
            "sha": "abb3ec1b8174043d5cd21d21fbe3c3fb3e9a11c7ceff3314a3222404feedda52",
            "nm": "phkkrw.ext",
            "ph": "/efvrfutgp/expgh/phkkrw",
            "dp": 2
        }
]


def test_process_json_log():
    expected_output = dict({"ext": 1, "pdf": 1})
    file_ext_to_name = praser.process_json_log(sample_json_log)
    actual_output = praser.get_file_ext_to_file_name_count(file_ext_to_name)
    assert expected_output == actual_output


def test_more_json_log():
    more_json_log = copy.deepcopy(sample_json_log)
    more_json_log = more_json_log + [
            {
                "ts": 1551140352,
                "pt": 55,
                "si": "3380fb19-0bdb-46ab-8781-e4c5cd448074",
                "uu": "0dd24034-36d6-4b1e-a6c1-a52cc984f105",
                "bg": " 77e28e28-745a-474b-a496-3c0e086eaec0",
                "sha": "abb3ec1b8174043d5cd21d21fbe3c3fb3e9a11c7ceff3314a3222404feedda52",
                "nm": "asdf.png",
                "ph": "/efvrfutgp/asdf.png",
                "dp": 2
            },
            {
                "ts": 1551140352,
                "pt": 55,
                "si": "3380fb19-0bdb-46ab-8781-e4c5cd448074",
                "uu": "0dd24034-36d6-4b1e-a6c1-a52cc984f105",
                "bg": "77e28e28-745a-474b-a496-3c0e086eaec0",
                "sha": "abb3ec1b8174043d5cd21d21fbe3c3fb3e9a11c7ceff3314a3222404feedda52",
                "nm": "phkkrw.jpg",
                "ph": "/efvrfutgp/expgh/phkkrw.jpg",
                "dp": 2
            },
            {
                "ts": 1551140352,
                "pt": 55,
                "si": "3380fb19-0bdb-46ab-8781-e4c5cd448074",
                "uu": "0dd24034-36d6-4b1e-a6c1-a52cc984f105",
                "bg": "77e28e28-745a-474b-a496-3c0e086eaec0",
                "sha": "abb3ec1b8174043d5cd21d21fbe3c3fb3e9a11c7ceff3314a3222404feedda52",
                "nm": "test.jpg",
                "ph": "/efvrfutgp/expgh/test.jpg",
                "dp": 3
            }
    ]

    expected_output = dict({"ext": 1, "pdf": 1, "jpg": 2, "png": 1})
    file_ext_to_name = praser.process_json_log(more_json_log)
    actual_output = praser.get_file_ext_to_file_name_count(file_ext_to_name)
    assert expected_output == actual_output


def test_malformed_json_log():
    malformed_json_log = copy.deepcopy(sample_json_log)
    malformed_json_log = malformed_json_log + [
        {
            "ts": "invalid timestamp",
            "pt": "55",
            "si": "3380fb19-0bdb-46ab-8781-e4c5cd448074",
            "uu": "0dd24034-36d6-4b1e-a6c1-a52cc984f105",
            "bg": "77e28e28-745a-474b-a496-3c0e086eaec0",
            "sha": "abb3ec1b8174043d5cd21d21fbe3c3fb3e9a11c7ceff3314a3222404feedda52",
            "nm": "abc.jpg",
            "ph": "/efvrfutgp/expgh/phkkrw.jpg",
            "dp": 2
        },
        {
                "ts": "invalid timestamp",
                "pt": "invalid pt",
                "si": "3380fb19-0bdb-46ab-8781-e4c5cd448074",
                "uu": "0dd24034-36d6-4b1e-a6c1-a52cc984f105",
                "bg": " 77e28e28-745a-474b-a496-3c0e086eaec0",
                "sha": "abb3ec1b8174043d5cd21d21fbe3c3fb3e9a11c7ceff3314a3222404feedda52",
                "nm": "asdf.png",
                "ph": "/efvrfutgp/asdf.png",
                "dp": 2
        }
    ]
    expected_output = dict({"ext": 1, "pdf": 1})
    file_ext_to_name = praser.process_json_log(malformed_json_log)
    actual_output = praser.get_file_ext_to_file_name_count(file_ext_to_name)
    assert expected_output == actual_output


def test_invalid_dp_field_value():
    malformed_json_log = copy.deepcopy(sample_json_log)
    malformed_json_log = malformed_json_log + [
        {
            "ts": "invalid timestamp",
            "pt": "55",
            "si": "3380fb19-0bdb-46ab-8781-e4c5cd448074",
            "uu": "0dd24034-36d6-4b1e-a6c1-a52cc984f105",
            "bg": "77e28e28-745a-474b-a496-3c0e086eaec0",
            "sha": "abb3ec1b8174043d5cd21d21fbe3c3fb3e9a11c7ceff3314a3222404feedda52",
            "nm": "abc.jpg",
            "ph": "/efvrfutgp/expgh/phkkrw.jpg",
            "dp": 1000000000000000
        },
        {
            "ts": "invalid timestamp",
            "pt": "invalid pt",
            "si": "3380fb19-0bdb-46ab-8781-e4c5cd448074",
            "uu": "0dd24034-36d6-4b1e-a6c1-a52cc984f105",
            "bg": "77e28e28-745a-474b-a496-3c0e086eaec0",
            "sha": "abb3ec1b8174043d5cd21d21fbe3c3fb3e9a11c7ceff3314a3222404feedda52",
            "nm": "asdf.png",
            "ph": "/efvrfutgp/asdf.png",
            "dp": -99999
        }
    ]
    expected_output = dict({"ext": 1, "pdf": 1})
    file_ext_to_name = praser.process_json_log(malformed_json_log)
    actual_output = praser.get_file_ext_to_file_name_count(file_ext_to_name)
    assert expected_output == actual_output

