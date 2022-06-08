import csv
import base64
import math
from search import search
from resourceversion import resource
from resourcecontent import resourcecontent
from app.methods import getkey, merge, checkkey

class generatecsv:
    def Generatecsv(auth_list, environ):
        resource_list = []
        search_keys_list = ['path', 'description', 'itemType', 'itemName', 'itemId']
        resource_keys_list = ['projectId', 'versionMajor', 'versionMinor', 'resVerId', 'state']
        search_response = search(auth_list).Search()
        for item in search_response:
            item = getkey(item, search_keys_list)
            resource_response = resource(auth_list,item['itemId']).Resource()
            if checkkey(resource_response, 'id', 1210):
                resource_response = {key: None for key in resource_keys_list}
            else:
                resource_response = getkey(resource_response, resource_keys_list)
            #resource_size = (len(base64.b64encode(bytes(resourcecontent(auth_list,resource_response['resVerId']).ResourceContent(),'utf-8')))*3)/4
            #resource_size = (math.ceil(resource_size/1024))
            #resource_list.append(merge(item, resource_response,{'size':resource_size}))
            resource_list.append(merge(item, resource_response))
        with open('{}.csv'.format(environ), 'w', newline='') as f:
            writer = csv.writer(f)
            count = 0
            for row in resource_list:
                if count == 0:
                # Writing headers to CSV file
                    headers = row.keys()
                    writer.writerow(headers)
                    count += 1
                # Writing rows to CSV file
                writer.writerow(row.values())
            return f.name