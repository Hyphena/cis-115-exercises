SPEED = 70.0
HOUR_1 = 6
HOUR_2 = 10
HOUR_3 = 15

print('A car is traveling down the interstate at 70mph, here is how far\n'
    'it would travel after x hours under optimal conditions:')
print(f'   After {HOUR_1:2,d} hours: {SPEED * HOUR_1:8,.1f} miles') # distance = speed * time
print(f'   After {HOUR_2:2,d} hours: {SPEED * HOUR_2:8,.1f} miles')
print(f'   After {HOUR_3:2,d} hours: {SPEED * HOUR_3:8,.1f} miles')
