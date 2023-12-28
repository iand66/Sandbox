from datetime import datetime as d
date = d.now()
day = date.strftime("%d")
month = date.strftime("%m")
year = date.strftime("%Y")

name = 'Ian'
age = 57
weight = 88.45051215000001
win_rate = 0.67
winnings = 201000000

# print(f'{name} is {age} years of age and weighs {weight} kg')
# print(f'{name} is {age:x} years of age and weighs {weight:.2f} kg') # Age in hex
# print(f'{name} is {age:b} years of age and weighs {weight:.2f} kg') # Age in binary
# print(f'{name} is {age} years of age and weighs {weight:.4f} kg')
# print(f'{name} is {age} years of age and weighs {weight:.2f} kg {name} wins {win_rate:.2%} of the time')
# print(f'{name} won £{winnings:,} on the Euro lottery on the {day} {month} {year}')

sentence = 'Each column has a width of ten'
table = ''
for word in sentence.split(' '):
    table += f'{word:.<10}' # < Left align / > Right align / ^ Centered
print(table)