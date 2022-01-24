TAX_RATE = 0.07
itemOnePrice = float(input('Enter the price of item 1: '))
itemTwoPrice = float(input('Enter the price of item 2: '))
itemThreePrice = float(input('Enter the price of item 3: '))
itemFourPrice = float(input('Enter the price of item 4: '))
itemFivePrice = float(input('Enter the price of item 5: '))

subTotal = itemOnePrice + itemTwoPrice + itemThreePrice + \
    itemFourPrice + itemFivePrice
salesTax = subTotal * TAX_RATE

print('---------------------------------------') # visual divider
print('SUBTOTAL'.rjust(26), f'${subTotal:,.2f}')
print('TAX'.rjust(26), f'${salesTax:,.2f}')
print('TOTAL'.rjust(26), f'${subTotal+ salesTax:,.2f}')
