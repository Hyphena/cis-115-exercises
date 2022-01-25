males = int(input('Please enter the number of males in your class: '))
females = int(input('Please enter the number of females in your class: '))
male_percent = males / (males + females)
fem_percent = females / (males + females)

print('   Classroom Percentages')
print(f'    Male:\t{male_percent:>6.1%}')
print(f'    Female:\t{fem_percent:>6.1%}')
