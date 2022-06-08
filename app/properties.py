class properties:
    def __init__(self,prop_dict):
        self.environ = prop_dict['environ']
        self.tenancy = prop_dict['tenancy']
        self.ck = prop_dict['client_key']
        self.cs =prop_dict['client_secret']