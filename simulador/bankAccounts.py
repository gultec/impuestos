import uuid

class BankAccount:
  def __init__(self):
    self.id = uuid.uuid4() # id único y aleatorio
    self.debitBalance = 0  # deber de la cuenta
    self.creditBalance = 0 # haber de la cuenta    
    self.interestRate = 0  # tasa de interés

  def credit(self, amount):
    self.creditBalance = self.creditBalance + amount
    self.debit(amount * -1)

  def debit(self, amount):
    self.debitBalance = self.debitBalance + amount
    self.credit(amount * -1)

