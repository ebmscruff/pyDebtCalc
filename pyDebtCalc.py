#!/usr/bin/python

import os
import csv
from debt import Debt as Debt

""" 
define debts - comment out to not use
Place in the order they should be paid off
when one is paid off, money will go to the next in line.
tpay = TOTAL PAYMENT = how much to pay per month total
"""
datafiles = ["./data/debts"]
initfiles = ["./data/initial"]
debts = []

for file in datafiles:
    if os.path.isfile(file):
        myFile = open(file) # Open the file
        myData = csv.reader(myFile) # CSVReader to take in data
        myDebtList = list(myData) # Make list from data
    else:
        print("Invalid file: {0}, exiting".format(file))
        exit()

    # For each item in list, create an object and make a list
    for item in myDebtList:
        if len(item) == 4: 
            debts.append(Debt(item[0], float(item[1]), float(item[2]), float(item[3])))
        if len(item) == 5: # 5 items if bills on that card
            debts.append(Debt(item[0], float(item[1]), float(item[2]), float(item[3]), float(item[4])))

for file in initfiles:
    if os.path.isfile(file):
        myFile = open(file)
        myData = csv.reader(myFile)
        myInitialData = list(myData)
    else:
        print("Invalid file: {0}, exiting".format(file))
        exit()


currentpath = float(myInitialData[0][0])
currentdebt = float(myInitialData[0][1])

tpay = 0
for debt in debts:
    tpay += debt.payment
#tpay = float(myInitialData[0][2])

""" get total monthly payement at outset """


totaldebt = 0
for debt in debts:
    totaldebt += debt.balance
print("total debt in this configuration: {0:.2f}".format(totaldebt))



counter = 0
test = True

def month():
    """
    make sure no debts without balance get paid
    """
    livedebts = []
    def debt_amount_audit(fulllist, livelist):
        for debt in fulllist:
            if debt.balance > 1:
                livelist.append(debt)
            elif debt.paidoff == 0: 
                print("**\nCongratulations, debt has been paid off! : {0}\n**".format(debt.name))
                debt.paidoff = 1
        if len(livelist) < 1:
            return False

    def pay_audit(livelist):
        total = 0
        for debt in livelist:
            if debt.payment > debt.balance:
                debt.payment = debt.balance
            total += debt.payment


        if total < tpay:
            remainder = tpay - total
            for debt in livelist:
                if debt.payment < debt.balance:
                    if debt.payment + remainder <= debt.balance:
                        debt.payment += remainder
                        remainder = 0 
                    else: 
                        diff = debt.balance - debt.payment
                        debt.payment += diff
                        remainder -= diff



        total = 0
        for debt in livelist:
            total += debt.payment

        if total > tpay:
            print("ERROR: Total payments ({0:.2f}) exceeded tpay ({1:.2f})".format(total, tpay))
            for debt in livelist:
                print("Name: {0}, Payment: {1:.2f}".format(debt.name, debt.payment))
            exit()
        else:
            print("Total scheduled to be paid this month: {0:.2f}".format(total))




    def do_payments(livelist):
        for debt in livedebts:
            debt.month()
        return True

    x = debt_amount_audit(debts, livedebts)
    if x == False: 
        return False
    x = pay_audit(livedebts)
    if x == False:
        return False
    x = do_payments(livedebts)
    if x == False:
        return False
    
    return True

while test == True:
    test = month()
    counter += 1
    print("    Months simulated: {0}".format(counter))

if test == False:
    globalpaid = 0
    for debt in debts:
        globalpaid += debt.totalpaid
    debtdiff = (currentdebt - totaldebt)
    print("    Original total debt: {0:.2f}".format(currentdebt))
    print("    Original expected amount paid: {0:.2f}".format(currentpath))
    print("    Debt in this configuration: {0:.2f}".format(totaldebt))
    print("    Paid in this configuration including lump sum: {0:.2f}".format(globalpaid + debtdiff))
    print("    Paid in this configuration after lump sum: {0:.2f}".format(globalpaid))
    print("    Amount written off: {0:.2f}".format(debtdiff))
    print("    Interest saved: {0:.2f}".format((currentpath - (globalpaid + debtdiff))))
