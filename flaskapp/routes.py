from flask import request, jsonify
from flaskapp import app, generatecsv_requestBodySchema, getcmsfolders_requestBodySchema
from main import createcsv, comparecsv, getfolders
from jsonschema import validate, ValidationError


def validateJson(jsonData,schema):
    try:
        validate(instance=jsonData, schema=schema)
    except ValidationError as err:
        return [False,{'errmsg': err.message}]
    return [True,'']

@app.route('/getcmsfolders' ,methods=['GET',])
def getcmsfolders():
    if request.method == 'GET':
        jsonData = request.get_json()
        isValid = validateJson(jsonData,getcmsfolders_requestBodySchema)
        if isValid[0]:
            return jsonify(getfolders.getfolders(jsonData))
        else:
            return jsonify(isValid[1]), 400

@app.route('/generatecsv' ,methods=['GET',])
def generate_csv():
    if request.method == 'GET':
        return 'Working'
        '''jsonData = request.get_json()
        isValid = validateJson(jsonData)
        if isValid[0]:
            csvnames_list = createcsv.createcsv()
            return csvnames_list
        else:
            return jsonify(isValid[1]), 400'''
        
@app.route('/generatecsvcompare' ,methods=['POST',])
def compare_csv():
    if request.method == 'POST':
        if "file1" in request.form and request.form['file1'] !=  "" :
                file1 = request.form['file1']
        else:
            return {'errormsg' : 'Please provide file1 name to compare'}, 400

        if "file2" in request.form and request.form['file2'] !=  "" :
                file2 = request.form['file2']
        else:
            return {'errormsg' : 'Please provide file2 name to compare'}, 400

    return comparecsv.comparecsv([file1, file2])