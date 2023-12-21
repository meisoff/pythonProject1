from abc import ABC, abstractmethod
from energy_consumer import EnergyConsumer


# Абстрактная фабрика для создания энергопотребителей
class EnergyConsumerFactory(ABC):
    @abstractmethod
    def create_energy_consumer(self, name: str) -> EnergyConsumer:
        pass


# Фабрика для создания промышленных энергопотребителей
class IndustrialEnergyConsumerFactory(EnergyConsumerFactory):
    def create_energy_consumer(self, name: str) -> EnergyConsumer:
        return EnergyConsumer(f"Промышленный {name}")


# Фабрика для создания домашних энергопотребителей
class HomeEnergyConsumerFactory(EnergyConsumerFactory):
    def create_energy_consumer(self, name: str) -> EnergyConsumer:
        return EnergyConsumer(f"Домашний {name}")
