post_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "title": {
            "type": "string"
        },
        "body": {
            "type": "string"
        },
        "userId": {
            "type": "integer"
        },
        "id": {
            "type": "integer"
        }
    },
    "required": [
        "title",
        "body",
        "userId",
    ]
}

put_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "title": {
            "type": "string"
        },
        "body": {
            "type": "string"
        },
        "userId": {
            "type": "integer"
        },
        "id": {
            "type": "integer"
        }
    },
    "required": [
        "id",
        "title",
    ]
}
