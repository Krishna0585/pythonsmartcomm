import json
def parseJson(jsonString):
    return json.loads(jsonString.strip('while(1);'))
def getkey(dict, keys):
    return {key: dict[key] for key in keys}
def merge(dict1, dict2):
    return {**dict1, **dict2}
def checkkey(dict, key, value):
    if key in dict.keys():
        if dict[key] == value:
            return True
    else:
        return False