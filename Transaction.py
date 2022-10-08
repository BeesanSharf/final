class Transaction:
    __id=0
    __date=''
    __client_id=0
    __account_id=0
    __type=''
    __amount = 0

    def __init__(self, id, date, client_id, account_id, type , amount):
        self.__id = id
        self.__date = date
        self.__client_id = client_id
        self.__account_id = account_id
        self.__type = type
        self.__amount = amount

    def getId(self):
        return self.__id

    def getDate(self):
        return self.__date

    def getClient_id(self):
        return self.__client_id

    def getAccount_id(self):
        return self.__account_id

    def getType(self):
        return self.__type
    def getAmount(self):
        return self.__amount

    def setId(self, id):
        self.__id = id

    def setDate(self, date):
        self.__date = date

    def setClientId(self, client_id):
        self.__client_id = client_id

    def setAccountId(self, account_id):
        self.__account_id = account_id

    def setType(self, type):
        self.__type= type
        def setAmount(self, amount):
            self.__amount= amount
