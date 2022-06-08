from app.methods import parseJson
def searchapi(tenancy, auth):
    url="https://{0}.smartcommunications.cloud/one/oauth1/cms/v8/search".format(tenancy)
    if tenancy == 'na4':
        folderId = 158042343
    else:
        folderId = 690144571
    params = {
            'recursive' : True,
            'start' : -1,
            'limit' : -1,
            'folderId' : folderId
        }
    header={
            'Accept':'application/json'
        }
    resp = auth.get(url=url,params=params,headers=header)
    return parseJson(resp.text)

def resourceversionapi(tenancy,auth,resourceid):
    url="https://{0}.smartcommunications.cloud/one/oauth1/cms/v8/resources/{1}/latestversion".format(tenancy,resourceid)
    params = {
            'projectScope' : 'ALL'
        }
    header={
            'Accept':'application/json'
        }
    resp = auth.get(url=url,params=params,headers=header)
    return parseJson(resp.text)

def getcontentapi(tenancy,auth,resourceversionid):
    url="https://{0}.smartcommunications.cloud/one/oauth1/cms/v8/versions/{1}/content".format(tenancy,resourceversionid)
    header={
            'Accept':'application/xml'
        }
    resp = auth.get(url=url,headers=header)
    return resp.text

def getcmsfolders(tenancy,auth):
    url="https://{0}.smartcommunications.cloud/one/oauth1/cms/v8/folders".format(tenancy)
    header={
            'Accept':'application/json'
        }
    resp = auth.get(url=url,headers=header)
    return resp.text