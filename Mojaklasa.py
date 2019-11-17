class Dog:


    def __init__(self):
        pass

    def voice(self):
        print('Gaaf')
    

class Cat:

    

    def __init__(self, wysokosc):
        self.wysokosc = wysokosc

    def voice(self):
        print(f"{self.wysokosc} cat seysMew")


if __name__ =='__main__':
    dog = Dog()
    cat = Cat(12)

    dog.voice()
    cat.voice()

    print(cat.wysokosc)