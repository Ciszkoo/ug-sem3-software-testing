import unittest

from ..CompanyAccount import CompanyAccount
from ..Account import Account

class TestExpressTransfer(unittest.TestCase):
  name = "Johny"
  surname = "Krasinski"
  pesel = "01212567891"
  company_name = "Januszex sp. z o.o."
  nip = "1234567890"

  def test_express_transfer_normal_account(self):
    account = Account(self.name, self.surname, self.pesel)
    account._balance = 100
    account.express_transfer(100)

    self.assertEqual(account.balance, -1, "Prowizja za przelew ekspresowy nie zostala pobrana!")

  def test_express_transfer_normal_account_not_enough_money(self):
    account = Account(self.name, self.surname, self.pesel)
    account._balance = 100
    account.express_transfer(101)

    self.assertEqual(account.balance, 100, "Przelew ekspresowy zostal zaksiegowany mimo braku srodkow!")

  def test_express_transfer_company_account(self):
    account = CompanyAccount(self.company_name, self.nip)
    account._balance = 100
    account.express_transfer(100)

    self.assertEqual(account.balance, -5, "Prowizja za przelew ekspresowy nie zostala pobrana!")

  def test_express_transfer_company_account_not_enough_money(self):
    account = CompanyAccount(self.company_name, self.nip)
    account._balance = 100
    account.express_transfer(101)

    self.assertEqual(account.balance, 100, "Przelew ekspresowy zostal zaksiegowany mimo braku srodkow!")