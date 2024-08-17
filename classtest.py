
# - The string representation of an object WITH the __str__() function

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("SAJIN", 21)

print(p1)

# O/P - SAJIN(21)