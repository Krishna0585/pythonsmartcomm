import json
import csv
from requests_oauthlib import OAuth1Session
from app.properties import properties
from app.methods import merge,getkey
from cmsfolders import folderlist
from generatecsv import generatecsv
from datetime import datetime as dt

class getfolders:
    def getfolders(json_list):
        for json_obj in json_list:
                xp = properties(json_obj)
                auth = OAuth1Session(client_key= xp.ck ,client_secret=xp.cs)
                auth_list = [xp.tenancy,auth]
                return json.loads(folderlist(auth_list).folderlist())
class comparecsv:
    def comparecsv(csvnames_list):
        each_csv_list = []
        csv_list = []
        first_csv_data = []
        flag = True
        for each_csvname in csvnames_list:
            try:
                with open(each_csvname , 'r', newline='') as f:
                    reader = csv.DictReader(f)
                    for item in reader:
                        if flag == True:
                            first_csv_data.append(item) 
                        else:
                            pass
                        each_csv_list.append(str(item['itemId'])+str(item['resVerId']))    
                    flag = False
                    csv_list.append(each_csv_list)
                    each_csv_list = []
            except FileNotFoundError:
                return {'errormsg' : 'File {} not found'.format(each_csvname)}, 400
        with open('Comparision_Output.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            headers = merge(first_csv_data[0],{'Flag': 'True'}).keys()
            writer.writerow(headers)
            for idx , val in enumerate(csv_list[0]):
                if val in csv_list[1]:
                    writer.writerow(merge(first_csv_data[idx],{'Flag': True}).values())
                else:
                    writer.writerow(merge(first_csv_data[idx],{'Flag': False}).values())
        return {
            'message' : 'Comparision done successfully',
            'filename' : 'Comparision_Output.csv'
        }

class createcsv:
    def createcsv():
        csvnames_list = []
        with open('properties.json' , 'r') as f:
            json_list = json.load(f)
            for json_obj in json_list:
                xp = properties(json_obj)
                auth = OAuth1Session(client_key= xp.ck ,client_secret=xp.cs)
                auth_list = [xp.tenancy,auth]
                csvnames_list.append(generatecsv.Generatecsv(auth_list, xp.environ))
                return generatecsv.Generatecsv(auth_list, xp.environ)
        return {'csv_names': csvnames_list}
        #return csvnames_list

if(__name__=='__main__'):
    print(dt.now())
    csvnames_list = createcsv.createcsv()
    print(csvnames_list)
    print(dt.now())
    print(comparecsv.comparecsv(csvnames_list))
    print(dt.now())