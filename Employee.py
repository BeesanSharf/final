from Person import Person


class Employee(Person):
    __emplyment_type = ''


    def __init__(self, ID, FullName, Age, id_no ,emplyment_type):
        self.emplyment_type = emplyment_type
        Person.__init__(self, ID, FullName, Age , id_no )

    def getEmplyment_type(self):
        return self.emplyment_type

    def setEmplyment_type(self, emplyment_type):
        self.emplyment_type = emplyment_type