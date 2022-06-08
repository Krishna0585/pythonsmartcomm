from smartcommapi import getcontentapi
class resourcecontent:
    def __init__(self, auth_list, resourceversionid):
        self.tenancy = auth_list[0]
        self.auth = auth_list[1]
        self.resourceversionid = resourceversionid
    def ResourceContent(self):
        return getcontentapi(self.tenancy,self.auth,self.resourceversionid)