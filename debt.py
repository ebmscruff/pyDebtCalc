#!/usr/bin/python

class Debt():
    def __init__(self, name="null", balance=0, apr=0, payment=0, bills=0):
        self.name = name
        self.balance = balance
        self.apr = apr
        self.payment = payment
        self.week = 0
        self.bills = bills
        self.paidoff = 0
        self.totalpaid = 0

    def month(self):
        if self.balance <= 0:
            print("Error: Payment called on paid-off card: {0}".format(self.name))
            return 0
        else:
            interest = ((self.balance * self.apr) / 12)
            self.balance -= self.payment
            self.totalpaid += self.payment
            self.week += 1
            print("Debt: {0}\nAPR: {1}, Interest: {2:.2f}".format(self.name, self.apr, interest))
            print("Week {0} : Paid {1:.2f} : Your new balance: {2:.2f}".format(self.week, self.payment, self.balance))
            interest = ((self.balance * self.apr) / 12)
            if self.balance > 0:
                self.balance += interest
                self.balance += self.bills
            return 1


