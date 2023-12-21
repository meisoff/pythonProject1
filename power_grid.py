# Класс, представляющий состояние энергосети
class PowerGrid:
    def __init__(self):
        self.observers = []  # Наблюдатели

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)


# Наблюдатель, отслеживающий загрузку энергосети
class LoadObserver:
    def __init__(self, name: str):
        self.name = name

    def update(self, message):
        print(f"{self.name}: {message}")


# Наблюдатель, отслеживающий неисправности в энергосети
class FaultObserver:
    def __init__(self, name: str):
        self.name = name

    def update(self, message):
        print(f"{self.name}: {message}")