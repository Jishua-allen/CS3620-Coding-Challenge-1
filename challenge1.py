print('******Part 1: Calculating simple interest******\n')

while True:
    try:
        principle = int(input('please enter your principle:\n'))
        numberOfYears = int(input('please enter the number of years:\n'))
        interest = int(input('please enter the interest rate:\n'))
        break
    except ValueError:
        print('Invalid input')

simpleInterest = (principle * numberOfYears * interest) / 100
print (f'Interest after {numberOfYears} would be: ${simpleInterest}\n\n\n')
        

print('******Part 2: List of my favorite Foods******\n')

favoriteFoods = ['Tater tot casserole', 'Steak and potatoes', 'Navajo Tacos(Scones)', 'Cheesy Taco Rice', 'Shephards Pie']
print('My Top 5 favorite foods:')
print(*favoriteFoods, sep="\n")
print(f'\n\n3rd in my list: {favoriteFoods[2]}')

favoriteFoods.append('Breakfast Burritos')
favoriteFoods.append('French toast')

print('\n\nNew list with some additions:')
print(*favoriteFoods, sep="\n")

favoriteFoods.insert(3, 'tacos')
print("\n\nYou Can't forget tacos, inserted at index 3")
print(*favoriteFoods, sep="\n")


print('\n\n******Part 3: Using For loops and Range function******\n')
list = ['I am a programmer', 'I am a programmer', 'I am a programmer', 'I am a programmer', 'I am a programmer']
print('For Loop:')
for x in list:
    print(x)

print('\n\nUsing Range:')
for x in range(0, 5):
    print('I am a programmer')
    

print('\n\nPrinting the squares of all numbers 1-9 (number: number^2)')

def printing_squares():
    for x in range(1, 10):
        print(f'{x} : {x * x}')

printing_squares()

