import random

class Animal:

    name = ''
    type = ''
    weight = 0

    def feed(self):
        return ('Покормили')

    def voice(self):
        if self.type == 'корова':
            return('Муууу!')
        elif self.type == 'овца':
            return('Бееее!')
        elif self.type == 'коза':
            return('Мееее!')
        elif self.type == 'гусь':
            return('Га-га-га!')
        elif self.type == 'курица':
            return('Ко-ко-ко!')
        elif self.type == 'утка':
            return('Кря-кря!')

class Bird(Animal):
    
    def eggs(self):
            return('Собрали яйца')

class Dairy(Animal):

    def milk(self):
            return('Подоили')

class Woolly(Animal):

    def cut(self):
            return('Постригли')

animals = []
for animal in range(10):
    animals.append(Animal())

animals[0] = Dairy()
animals[0].name = 'Манька'
animals[0].type = 'корова'

animals[1] = Woolly()
animals[1].name = 'Барашек'
animals[1].type = 'овца'

animals[2] = Woolly()
animals[2].name = 'Кудрявый'
animals[2].type = 'овца'

animals[3] = Dairy()
animals[3].name = 'Рога'
animals[3].type = 'коза'

animals[4] = Dairy()
animals[4].name = 'Копыта'
animals[4].type = 'коза'

animals[5] = Bird()
animals[5].name = 'Серый'
animals[5].type = 'гусь'

animals[6] = Bird()
animals[6].name = 'Белый'
animals[6].type = 'гусь'

animals[7] = Bird()
animals[7].name = 'Ко-ко'
animals[7].type = 'курица'

animals[8] = Bird()
animals[8].name = 'Кукареку'
animals[8].type = 'курица'

animals[9] = Bird()
animals[9].name = 'Кряква'
animals[9].type = 'утка'

for animal in animals:
    print(animal.type)
    print(animal.name)
    animal.weight = random.randint(1,10)
    print(animal.weight)
    print(animal.feed())
    print(animal.voice())
    print()
