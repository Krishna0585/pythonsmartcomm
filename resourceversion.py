from smartcommapi import resourceversionapi
class resource:
    def __init__(self, auth_list, resourceid):
        self.tenancy = auth_list[0]
        self.auth = auth_list[1]
        self.resourceid = resourceid
    def Resource(self):
        return resourceversionapi(self.tenancy,self.auth,self.resourceid)