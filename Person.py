class Person:
    __ID = ''
    __FullName = ''
    __Age = 0
    __id_no = ''

    def __init__(self, ID, FullName, Age ,id_no):
        self.__ID = ID
        self.__FullName = FullName
        self.__Age = Age
        self.id_no = id_no

    def getID(self):
        return self.__ID

    def getFullName(self):
        return self.__FullName

    def getAge(self):
        return self.__Age
    def getId_No(self):
        return self.__id_no

    def setID(self, ID):
        self.__ID = ID

    def setFullName(self, FullName):
        self.__FullName = FullName

    def setAge(self, Age):
        self.__Age = Age

    def setId_No(self, id_no):
        self.__id_no = id_no
