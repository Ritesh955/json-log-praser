JSON_LOG_RECORD_FIELD_COUNT = 9

JSON_LOG_RECORD_SCHEMA = {
    "type": "object",
    "properties": {
        "ts": {"type": "number"},
        "pt": {"type": "number"},
        "si": {"type": "string"},
        "uu": {"type": "string"},
        "bg": {"type": "string"},
        "sha": {"type": "string"},
        "nm": {"type": "string"},
        "ph": {"type": "string"},
        "dp": {"type": "number"},
    },
}