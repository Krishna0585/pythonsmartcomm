import os
from requests_oauthlib import OAuth1Session
from app.properties import properties
from app.methods import parseJson
json_obj = {
			"environ" : "hcloud",
			"tenancy" : "na4",
			"client_key" : "2a532d20-a490-448e-871d-52469e09922e!sysadmin@htcinc.com.partner",
	    	"client_secret" : "b08f0691-c906-4787-9bca-87b805682b9b"
		}

xp = properties(json_obj)
auth = OAuth1Session(client_key= xp.ck ,client_secret=xp.cs)
rid = 158029314
url="https://{0}.smartcommunications.cloud/one/oauth1/cms/v7/resources/{1}/latestversion".format(xp.tenancy,rid)
params ={
            'projectScope' : 'ALL'
        }
header ={
            'Accept':'application/json'
    	}
resp = auth.get(url=url,params=params,headers=header)
print(parseJson(resp.text))