# json-log-praser
This log parsing util validates json log lines, parses the values and generates unique file extensions to file names map. 
This map is then converted to file extensions to file counts. The intermediate json log state could serve another use case.

A json log record follows the below schema:

JSON format:
```

ts: timestamp

pt: processing time

si: session ID

uu: user UUID

bg: business UUID

sha: sha256 of the file

nm: file name

ph: path

dp: disposition (valid values: MALICIOUS (1), CLEAN (2), UNKNOWN (3))

```

Assumption: 

Valid Json record is such a record that contains all the above fields. The field values
should also follow the below field type mapping:

```
    "ts": {"type": "number"},
    "pt": {"type": "number"},
    "si": {"type": "string"},
    "uu": {"type": "string"},
    "bg": {"type": "string"},
    "sha": {"type": "string"},
    "nm": {"type": "string"},
    "ph": {"type": "string"},
    "dp": {"type": "number"},
```

About the project external dependencies/requirements:
* jsonschema
* nose
* pytest


Running the Tests:

* System requirement: python3.7

* cd to the root of the project

* python3 -m venv venv

* source venv/bin/activate

* pip install -r requirements.txt

* nosetests tests/unit/test_process_json_log.py

