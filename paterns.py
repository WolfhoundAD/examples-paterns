from abc import ABC, abstractmethod

#Singleton:
class Singleton:
    instance = None

    @staticmethod
    def getInstance():
        """Статический метод, который возвращает единственный экземпляр класса"""
        if Singleton.instance == None:
            Singleton()
        return Singleton.instance

    def __init__(self):
        """Приватный конструктор, который создает единственный экземпляр класса"""
        if Singleton.instance != None:
            raise Exception("Этот класс является Singleton-ом!")
        else:
            Singleton.instance = self

s = Singleton()
print(s)
s = Singleton.getInstance()
print(s)
s = Singleton.getInstance()
print(s)

#Factory Method:
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f"Создатель: Код того же создателя только что работал с {product.operation()}"
        return result

class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteProduct1(Product):
    def operation(self):
        return "{Результат ConcreteProduct1}"

class ConcreteProduct2(Product):
    def operation(self):
        return "{Результат ConcreteProduct2}"

def client_code(creator):
    print(f"Клиент: Я не знаю о классе creator, но он все еще работает.\n{creator.some_operation()}")

if __name__ == "__main__":
    print("Приложение: запущено с помощью ConcreteCreator1.")
    client_code(ConcreteCreator1())

    print("\n")

    print("Приложение: запущено с помощью ConcreteCreator2.")
    client_code(ConcreteCreator2())

#Observer:
class Subject:
    _state = 0
    _observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self):
        self._state = int(input("Введите число: "))
        self.notify()

class Observer:
    def update(self, subject):
        pass

class ConcreteObserverA(Observer):
    def update(self, subject):
        if subject._state < 3:
            print("ConcreteObserverA: отреагировал на событие")

class ConcreteObserverB(Observer):
    def update(self, subject):
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: отреагировал на событие")

subject = Subject()

observer_a = ConcreteObserverA()
subject.attach(observer_a)

observer_b = ConcreteObserverB()
subject.attach(observer_b)

subject.some_business_logic()
subject.some_business_logic()

subject.detach(observer_a)

subject.some_business_logic()


#Decorator:
class Component:
    def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"

class Decorator(Component):
    component1: Component = None

    def __init__(self, component: Component) -> None:
        self.component1 = component

    @property
    def component(self) -> str:
        return self.component1

    def operation(self) -> str:
        return self.component1.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"

class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"

def client_code(component: Component) -> None:
    print(f"Результат: {component.operation()}")

if __name__ == "__main__":
    simple = ConcreteComponent()
    print("Клиент: У меня есть простой компонент:")
    client_code(simple)
    print("\n")

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Клиент: Теперь у меня есть оформленный компонент:")
    client_code(decorator2)