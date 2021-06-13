class Student:
    def __init__(self,__id,__username,__password,__name,__address,__city,__pincode,__contact_number,__email):
        self.__id = __id
        self.__username = __username
        self.__password = __password
        self.__name = __name
        self.__address = __address
        self.__city = __city
        self.__pincode = __pincode
        self.__contact_number = __contact_number
        self.__email = __email

    def __str__(self):
        return "Id : {0}\nUser Name : {1}\nPassword : {2}\nName : {3}\nAddress : {4}\ncity : {5}\nPincode : {6}\nContact Number : {7}\nemail : {8}".format(self.__id, self.__username, self.__password, self.__name, self.__address, self.__city, self.__pincode, self.__contact_number, self.__email)
