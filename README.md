# pyDebtCalc
Python debt calculator

# How to use
There are two files that need to be updated:
 1. data/debts
    This is a CSV (comma separated values) file in the following format:
        Name , Balance , APR , Payment
    Update this file with your debts (and remove the example cards) and capture the the values of the following fields:
    -. Debt in this configuration
    -. Amount paid in this configuration
 2. data/initial
    This is a CSV (comma separated values) file in the following format:
        Original Total Debt , Original Amount to Payoff

    Fill in these fields with the values from the "Debts in this configuration" and "Amount Paid in this configuration" fields from your first run.
    
