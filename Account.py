class Account:
    __account_id = 0
    __balance = ''
    __owner_id = ''

    def __init__(self, account_id, balance, owner_id):
        self.__account_id = account_id
        self.__balance = balance
        self.__owner_id = owner_id

    def getAccountId(self):
        return self.__account_id

    def getBalance(self):
        return self.__balance

    def getOwnerId(self):
        return self.__owner_id

    def setAccountId(self, account_id):
        self.__account_id = account_id

    def setBalance(self, balance):
        self.__balance = balance

    def setOwnerId(self, owner):
        self.__owner_id = owner
