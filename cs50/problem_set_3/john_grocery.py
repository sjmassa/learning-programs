import sys

# Recieves a grocery item input from user
# Check for EOFError
def grocery_item():
    try:
        item = input()
    except EOFError:
        return 'exit'
    return item.lower()

# Prints alphabetically sorted grocery dictionary and exits
def print_groceries(groceries):
    for key, value in sorted(groceries.items()):
        print(f"{value} {key.upper()}")
    sys.exit()

# Repeats input() after valid or invalid user input
# Prints and exits program upon receiving an EOFError
def main():
    groceries = {}
    while True:
        num = 0
        item = grocery_item()
        if item == 'exit':
            print_groceries(groceries)
        # Adds grocery item to dictionary, incrementing existing items
        if item in groceries.keys():
            num = groceries.get(item) + 1
            groceries[item] = num
        else:
            groceries[item] = 1

if __name__ == "__main__":
    main()
