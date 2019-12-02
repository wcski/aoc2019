input = open('input', 'r')

inputSplit = input.read().split("\n")

def calculateFuel(mass):
    massNum = int(mass)
    fuel = round(massNum/3) - 2
    return fuel

def calculateFuelPartTwo(massPartTwo):
    fuelTank = calculateFuel(mass)
    finalFuel = 0
    while fuelTank > 0:
        finalFuel += fuelTank
        fuelTank = calculateFuel(fuelTank)
    return finalFuel

partTwoAnswer = 0

for mass in inputSplit:
    partTwoAnswer += calculateFuelPartTwo(mass)
    print partTwoAnswer