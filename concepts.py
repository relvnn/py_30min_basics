#--------------------------------------------------------
# Mensagem de boas-vindas
#--------------------------------------------------------
print("Mensagem de boas-vindas: Hello, World!")

#--------------------------------------------------------
# Declaração de variáveis com diferentes tipos de dados
#--------------------------------------------------------
number = 10  # Inteiro
decimal = 10.5  # Float (número decimal)
text = "Hello, World!"  # String
active = True  # Booleano

#--------------------------------------------------------
# Declaração de lista e dicionário
#--------------------------------------------------------
names: list = ["Alice", "Bob", "Charlie"]  # Lista de nomes
ages: dict = {"Alice": 24, "Bob": 30, "Charlie": 28}  # Dicionário mapeando nomes para idades

#--------------------------------------------------------
# Declaração de tupla e conjunto
#--------------------------------------------------------
coordinates: tuple = (10, 20)  # Tupla representando coordenadas
point: set = {10, 20}  # Conjunto contendo valores únicos

#--------------------------------------------------------
# Imprime os valores das variáveis no console
#--------------------------------------------------------
print(f"Valores das variáveis: {number}, {decimal}, {text}, {active}")
print(f"Lista de nomes: {names}")
print(f"Dicionário de idades: {ages}")

#--------------------------------------------------------
# Redefinição de variáveis com novos valores e anotações de tipo
#--------------------------------------------------------
number: int = 20  # Inteiro
decimal: float = 20.5  # Float
text: str = "Hello, Python!"  # String
active: bool = False  # Booleano

#--------------------------------------------------------
# Exemplo de incompatibilidade de tipo (isso causará um erro)
#--------------------------------------------------------
# numberError: int = "Hello, World!"  # Comentado para evitar erro

#--------------------------------------------------------
# Declaração de constantes
#--------------------------------------------------------
from typing import Final

PI: Final = 3.14159  # Valor de PI
G: Final = 9.81  # Constante de aceleração gravitacional

#--------------------------------------------------------
# Imprime a data e hora atual
#--------------------------------------------------------
from datetime import datetime
print(f"Data e hora atual: {datetime.now()}")

#--------------------------------------------------------
# Declaração de função com parâmetros e tipo de retorno
#--------------------------------------------------------
def add(a: int, b: int) -> int:
    return a + b

# Chama a função e imprime o resultado
result: int = add(10, 20)
print(f"Resultado da soma (10 + 20): {result}")

#--------------------------------------------------------
# Declaração de classes
#--------------------------------------------------------

# Classe Person
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Olá, meu nome é {self.name} e eu tenho {self.age} anos.")

# Classe Car
class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(f"Dirigindo o {self.make} {self.model}.")

    def display(self):
        print(f"Este é um {self.year} {self.make} {self.model}.")

    def getInformation(self):
        return f"{self.year} {self.make} {self.model}"
    
    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model}"
    
    def __add__(self, other: "Car") -> str:
        return f'{self.year + other.year} {self.make} {self.model}'

#--------------------------------------------------------
# Criação de instâncias e chamadas de métodos
#--------------------------------------------------------
BMW = Car("BMW", "X5", 2021)
print(f"Informações do carro BMW: {BMW.getInformation()}")

person = Person("Alice", 24)
person.greet()

car = Car("Toyota", "Corolla", 2020)
car.drive()
print(f"Informações do carro Toyota: {car.getInformation()}")
car.display()

print(f"Carro como string: {car}")

#--------------------------------------------------------
# Classe com métodos estáticos
#--------------------------------------------------------
class Math:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def subtract(a: int, b: int) -> int:
        return a - b

# Chama métodos estáticos da classe Math
print(f"Resultado da soma (10 + 20): {Math.add(10, 20)}")
print(f"Resultado da subtração (20 - 10): {Math.subtract(20, 10)}")

#--------------------------------------------------------
# Função com argumento opcional
#--------------------------------------------------------
def greet(name: str, message: str = "Olá") -> None:
    print(f"{message}, {name}!")

# Chama a função com um argumento
greet("Alice")