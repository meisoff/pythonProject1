from energy_consumer_factory import IndustrialEnergyConsumerFactory, HomeEnergyConsumerFactory
from power_grid import PowerGrid, LoadObserver, FaultObserver

if __name__ == "__main__":
    # Создаем объекты фабрик
    industrial_factory = IndustrialEnergyConsumerFactory()
    home_factory = HomeEnergyConsumerFactory()

    # Создаем энергопотребителей с помощью фабрик
    industrial_consumer = industrial_factory.create_energy_consumer("Станок")
    home_consumer = home_factory.create_energy_consumer("Холодильник")

    # Создаем объект энергосети
    power_grid = PowerGrid()

    # Создаем наблюдателей
    load_observer = LoadObserver("Наблюдатель загрузки")
    fault_observer = FaultObserver("Наблюдатель неисправностей")

    # Регистрируем наблюдателей в энергосети
    power_grid.add_observer(load_observer)
    power_grid.add_observer(fault_observer)

    # Загрузка энергосети
    power_grid.notify_observers("Энергосеть загружена на 70%")

    # Потребление энергии
    industrial_consumer.consume_energy()
    home_consumer.consume_energy()

    # Сообщение о неисправности
    power_grid.notify_observers("Обнаружена неисправность в энергосети!")
