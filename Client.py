from Person import Person


class Client(Person):
    __Phone_number = ''

    def __init__(self, ID, FullName, Age, id_no, Phone_number):
        self.Phone_number = Phone_number
        Person.__init__(self, ID, FullName,id_no,Age)

    def getPhone_number(self):
        return self.Phone_number

    def setPhone_number(self, Phone_number):
        self.__Phone_number = Phone_number
