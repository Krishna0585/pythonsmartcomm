from flask import Flask
app = Flask(__name__)
getcmsfolders_requestBodySchema = {
    "type": "array",
    "items": {
        "properties": {
            "environ": {"type": "string"},
            "tenancy": {"type": "string"},
            "client_key": {"type": "string"},
            "client_secret": {"type": "string"}
        },
        "required":["environ","tenancy","client_key","client_secret"],
    },
    "maxItems" : 1
}
generatecsv_requestBodySchema = {
    "type": "array",
    "items": {
        "properties": {
            "environ": {"type": "string"},
            "tenancy": {"type": "string"},
            "folderId":{"type": "array"},
            "client_key": {"type": "string"},
            "client_secret": {"type": "string"}
        },
        "required":["environ","tenancy","folderId","client_key","client_secret"],
    },
    "maxItems" : 1
}
from flaskapp import routes