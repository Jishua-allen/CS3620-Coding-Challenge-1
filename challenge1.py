print("Part 1: Calculating simple interest\n")


while True:
    try:
        principle = int(input("please enter your principle:\n"))
        numberOfYears = int(input("please enter the number of years:\n"))
        interest = int(input("please enter the interest rate:\n"))
        break
    except ValueError:
        print("Invalid input")

simpleInterest = (principle * numberOfYears * interest) / 100
print (f'Interest after {numberOfYears} would be: ${simpleInterest}')
        


