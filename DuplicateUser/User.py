class User:
    def __init__(self,name,username,password,mobile_number):
        self.name = name
        self.username = username
        self.password = password
        self.mobile_number = mobile_number

    def __eq__(self,obj):
        if isinstance(obj, User):
            #return self.name == obj.name
            return self.mobile_number == obj.mobile_number
