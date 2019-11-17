
class Employee:
    
    def __init__(self, days_per_week, position, coef, name):
        self.days_per_week = days_per_week
        self.position = position
        self.coef = coef
        self.name = name

    def get_salary(self):
        return (self.days_per_week*4*self.coef)



class Accounter(Employee):

    def __init__(self, name):
        self.days_per_week = 5
        self.position = "accounter"
        self.coef = 0.8
        self.name = name

class Chief(Employee):

    def __init__(self, name):
        self.days_per_week = 4
        self.position = "chief"
        self.coef = 2.5
        self.name = name

class Cleaner(Employee):

    def __init__(self, name):
        self.days_per_week = 6
        self.position = "cleaner"
        self.coef = 0.4
        self.name = name

class Driver(Employee):

    def __init__(self, name):
        self.days_per_week = 7
        self.position = "driver"
        self.coef = 0.3
        self.name = name

class Manager(Employee):

    def __init__(self, name):
        self.days_per_week = 3
        self.position = "manager"
        self.coef = 0.2
        self.name = name

class Postman(Employee):

    def __init__(self, name):
        self.days_per_week = 5
        self.position = "postman"
        self.coef = 0.7
        self.name = name

if __name__ =='__main__':

    chief = Chief("Patryk")
    cleaner = Cleaner("Mateusz")
    accounter = Accounter("Sylwia")
    driver = Driver("Adam")
    manager = Manager("Wojtek")
    postman = Postman("Pawel")

    #print(cleaner.name, cleaner.get_salary())

    pracownicy = [chief, cleaner, accounter, driver, manager, postman]
    print(lista)

    for pracownik in pracownicy:
        print(i.days_per_week, end=' ')
        print(i.position, end=' ')
        print(i.coef, end=' ')
        print(i.name)

    suma = 0

    for i in lista:
        suma = suma + i.get_salary()
            

    print(suma)  

        
    

