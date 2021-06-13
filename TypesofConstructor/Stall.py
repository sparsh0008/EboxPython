class Stall:

    def __init__(self, __name ="", __detail = ""):
        self.__name = __name
        self.__detail = __detail

    def get_name(self):
        return self.__name

    def get_detail(self):
        return self.__detail

    def set_name(self, name):
        self.__name = name

    def set_detail(self, detail):
        self.__detail = detail

    def __str__(self):
        return 'Book Name :' + self.__name + 'Detail :  ' +  self.__detail
