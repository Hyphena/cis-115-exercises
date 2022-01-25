SHARES_BOUGHT = 2000
BUY_PRICE = 40.00
BUY_COMMISSION_RATE = 0.03
SHARES_SOLD = 2000
SELL_PRICE = 42.75
SELL_COMISSION_RATE = 0.03

original_price = SHARES_BOUGHT * BUY_PRICE
buy_commission = original_price * BUY_COMMISSION_RATE
sale_price = SHARES_SOLD * SELL_PRICE
sale_commission = sale_price * SELL_COMISSION_RATE
profit = sale_price - original_price - buy_commission - sale_commission

print('   You originally paid:', f'${original_price:,.1f}'.rjust(12),
    sep='\t\t')
print('   The buying commission was:', f'${buy_commission:,.1f}'.rjust(12),
    sep='\t')
print('   You sold your stocks for:', f'${sale_price:,.1f}'.rjust(12),
    sep='\t')
print('   The sale commission was:', f'${sale_commission:,.1f}'.rjust(12),
    sep='\t')
print('   In the end you made a profit of:', f'${profit:,.1f}'.rjust(8))
