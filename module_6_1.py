class Animal: #животные
    alive = True # живой
    fed = False # голдный

    def __init__(self, name): # имя животного
        self.name = name


    def eat(self, food): # для животного съедобное или не съедобное растение и что из этого вышло
        if food.edible:
            print(f"{self.name} съел {food.name}")
            fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            alive = False


class Plant: # растения
    edible = False #не съедобное

    def __init__(self, name): #название растения
        self.name = name

class Mammal(Animal): #млекопитающее
    pass

class Predator(Animal): #хищники
    pass

class Flower(Plant): #цветы
    pass

class Fruit(Plant): #фрукты
    edible = True #съедобное


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)