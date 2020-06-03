import uuid

class Person:
  def __init__(self):
    self.id = uuid.uuid4() # id único y aleatorio
    self.age = 0           # edad en generaciones del simulador

class PhysicalPerson(Person):
  def __init__(self):
    self.type = "Physical"

class MoralPerson(Person):
  def __init__(self):
    self.type = "Moral"