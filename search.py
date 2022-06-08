from smartcommapi import searchapi
class search:
    def __init__(self, auth_list):
        self.tenancy = auth_list[0]
        self.auth = auth_list[1]
    def Search(self):
        return searchapi(self.tenancy, self.auth)