class Animal:
    def __init__(self, name="???", species="Объект живой природы"):
        self.name = name
        self.species = species

    def introduce(self):
        print(f"Я {self.species} по имени {self.name}")


class Fish(Animal):
    def __init__(self, name, fish_habitat="???"):
        super().__init__(name, species="Рыба")
        self.fish_habitat = fish_habitat

    def introduce(self):
        super().introduce()
        print(f"Я обитаю в {self.fish_habitat}")


class Bird(Animal):
    def __init__(self, name, is_flying=False):
        super().__init__(name, species="Птица")
        self.is_flying = is_flying

    def introduce(self):
        super().introduce()
        if self.is_flying:
            print("Я умею летать")
        else:
            print("Я не умею летать")


class Cat(Animal):
    def __init__(self, name, breed="???"):
        super().__init__(name, species="Кошка")
        self.breed = breed

    def introduce(self):
        super().introduce()
        print(f"Моя порода - это {self.breed}")


class AnimalFactory:
    def create_animal(self, animal_type, name, **kwargs):
        if animal_type == "Fish":
            return Fish(name, **kwargs)
        elif animal_type == "Bird":
            return Bird(name, **kwargs)
        elif animal_type == "Cat":
            return Cat(name, **kwargs)
        else:
            print("Такого животного не существует")


factory = AnimalFactory()
fish = factory.create_animal("Fish", "Немо", fish_habitat="море")
bird = factory.create_animal("Bird", "Чилли-Вилли", is_flying=False)
cat = factory.create_animal("Cat", "Барсик", breed="Бурманская кошка")

fish.introduce()
bird.introduce()
cat.introduce()
