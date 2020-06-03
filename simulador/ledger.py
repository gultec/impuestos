import uuid
import time

class Ledger:
  def __init__(self):
    self.ledgerId = uuid.uuid4()
    self.transactions = []


class Transaction()
  def __init__(self, srcAccount, dstAccount, amount):
    self.transactionId = uuid.uuid4()
    self.srcAccount = srcAccount
    self.dstAccount = dstAccount
    self.amount = amount
    self.timestamp = 0 # 0 es que no se ha ejecutado

  def execute(self)
    self.srcAccount.debit(self.amount)
    self.dstAccount.credit(self.amount)
    self.timestamp = time.time()