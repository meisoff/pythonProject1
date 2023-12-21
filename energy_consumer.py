from random import randint


# Класс, представляющий энергопотребителя
class EnergyConsumer:
    def __init__(self, name: str):
        self.name = name
        self.power_consumption = 0

    def consume_energy(self):
        self.power_consumption = randint(1, 100)
        print(f"{self.name} потребляет {self.power_consumption} единиц энергии.")

    def __str__(self):
        return f"{self.name} (Потребление: {self.power_consumption} единиц)"