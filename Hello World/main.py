import random

class Animal:

    name = ''
    type = ''
    weight = 0

    def feed(self):
        return ('Покормили')

    def eggs(self):
        if self.type in ('курица', 'утка','гусь'):
            return('Собрали яйца')
        else:
            return('Яиц не даёт')

    def milk(self):
        if self.type in ('корова', 'коза'):
            return('Подоили')
        else:
            return('Не доится')

    def cut(self):
        if self.type == 'овца':
            return('Постригли')
        else:
            return('Не стрижётся')

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

animals = []
for animal in range(10):
    animals.append(Animal())

animals[0].name = 'Манька'
animals[0].type = 'корова'

animals[1].name = 'Барашек'
animals[1].type = 'овца'

animals[2].name = 'Кудрявый'
animals[2].type = 'овца'

animals[3].name = 'Рога'
animals[3].type = 'коза'

animals[4].name = 'Копыта'
animals[4].type = 'коза'

animals[5].name = 'Серый'
animals[5].type = 'гусь'

animals[6].name = 'Белый'
animals[6].type = 'гусь'

animals[7].name = 'Ко-ко'
animals[7].type = 'курица'

animals[8].name = 'Кукареку'
animals[8].type = 'курица'

animals[9].name = 'Кряква'
animals[9].type = 'утка'

for animal in animals:
    print(animal.type)
    print(animal.name)
    animal.weight = random.randint(1,10)
    print(animal.weight)
    print(animal.voice())
    print(animal.feed())
    print(animal.eggs())
    print(animal.cut())
    print(animal.milk())
    print()

sum_weight = 0
max_weight = 0
heaviest = ''
for animal in animals:
    sum_weight += animal.weight
    if animal.weight > max_weight:
        max_weight = animal.weight
        heaviest = animal.name
print('Общий вес животных:', sum_weight)
print('Самое тяжёлое животное', heaviest)