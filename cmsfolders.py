from smartcommapi import getcmsfolders
class folderlist:
    def __init__(self, auth_list):
        self.tenancy = auth_list[0]
        self.auth = auth_list[1]
    def folderlist(self):
        return getcmsfolders(self.tenancy, self.auth)