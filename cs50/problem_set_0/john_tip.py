
#Takes user input of the cost of the meal and tip percent.
#Returns tip in dollars.
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    return f"Leave ${tip:.2f}"

#Remove $ and convert to float.
def dollars_to_float(d):
    cost_to_float = float(d[1:])
    return cost_to_float

#Remove % and convert to float and percent.
def percent_to_float(p):
    tip_to_float = float(p[:-1])/100
    return tip_to_float

if __name__ == '__main__':
    print(main())
