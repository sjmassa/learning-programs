import sys

# Felipe's Taqueria menu
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

# Accepts user input for a food item, case insensitive
# Checks for an EOFError
def get_input():
    while True:
        try:
            item_ordered = input("Item: ")
        except EOFError:
            sys.exit()
        for key, value in menu.items():
            if item_ordered.lower() == key.lower():
                return value

# Prints order total after each input
def main():
    order_total = 0
    while True:
        order_total += float(get_input())
        print(f"Total: ${order_total:.2f}")

if __name__ == "__main__":
    main()
