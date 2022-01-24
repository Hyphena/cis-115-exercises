TIP_RATE = 0.18
SALES_RATE = 0.07

sub_total = float(input('Please enter the amount paid: '))
tip_amount = sub_total * TIP_RATE
sales_tax = sub_total * SALES_RATE
total = sub_total + tip_amount + sales_tax

print('SUBTOTAL: '.rjust(12), f'${sub_total:,.2f}'.rjust(6))
print('SALES TAX: '.rjust(12), f'${sales_tax:,.2f}'.rjust(6))
print('TIP: '.rjust(12), f'${tip_amount:,.2f}'.rjust(6))
print('TOTAL: '.rjust(12), f'${total:,.2f}'.rjust(6))
