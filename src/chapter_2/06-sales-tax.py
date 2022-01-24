from itertools import count
from tkinter import W


STATE_RATE = 0.05
COUNTY_RATE = 0.025
purchase_amount = float(input('Please enter the amount paid: '))

state_tax = purchase_amount * STATE_RATE
county_tax = purchase_amount * COUNTY_RATE
total = purchase_amount + state_tax + county_tax

# honestly this is just a formatting mess, i apologize
#   output: AAAAAA:  $X,XXX.XX

print('SUBTOTAL: '.rjust(21), f'${purchase_amount:,.2f}'.rjust(7))
print('STATE SALES TAX: '.rjust(21), f'${state_tax:,.2f}'.rjust(7))
print('COUNTY SALES TAX: '.rjust(21), f'${county_tax:,.2f}'.rjust(7))
print('TOTAL: '.rjust(21), f'${total:,.2f}'.rjust(7))
