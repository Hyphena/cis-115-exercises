from unittest import result


principal = float(input('Please enter the amount of principal originally '
    'deposited: '))
annual_rate = float(input('Please enter the annual interest rate on the '
    'account (0.XX): '))
annual_compound = int(input('Please enter the number of times per year '
    'that the interest is compounded: '))
planned_time = int(input('Please enter the number of years you plan to '
    'accrue interest: '))
resulting_balance = principal * (1 + annual_rate / annual_compound) ** \
    (annual_compound * planned_time)

print(f'   After {planned_time} year(s), your account should hold:',
    f'${resulting_balance:,.2f}')
