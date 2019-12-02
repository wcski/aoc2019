input = open('input', 'r')

inputSplit = input.read().split("\n")

def calculateFuel(mass):
    massNum = int(mass)
    fuel = round(massNum/3) - 2
    return fuel

totalFuel = 0

for mass in inputSplit:
    totalFuel += calculateFuel(mass)
    print totalFuel