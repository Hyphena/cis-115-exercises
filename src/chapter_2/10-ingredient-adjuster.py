# calculate the ingredients needed for a singular cookie
SUGAR_FOR_ONE = 1.5 / 48
BUTTER_FOR_ONE = 1 / 48
FLOUR_FOR_ONE = 2.75 / 48
cookies_desired = int(input('How many cookies would you like to bake? '))

print(f'To bake {cookies_desired:,d} cookie(s) you will need:')
print(f'   - {SUGAR_FOR_ONE * cookies_desired:,.2f} cup(s) of sugar')
print(f'   - {BUTTER_FOR_ONE * cookies_desired:,.2f} cup(s) of butter')
print(f'   - {FLOUR_FOR_ONE * cookies_desired:,.2f} cup(s) of flour')
