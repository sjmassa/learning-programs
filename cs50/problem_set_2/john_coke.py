
# Receives input from user in increments of 25, 10, or 5
# While total user input is less than 50, function asks for more input
def get_50_cents():
    total_amount = 0
    while True:
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            continue
        if coin == 25 or coin == 10 or coin == 5:
            total_amount += coin
            if total_amount < 50:
                print(f"Amount Due: {50 - total_amount}")
                continue
            else:
                return total_amount - 50

def main():
    change = get_50_cents()
    return f"Change Owed: {change}"

if __name__ == '__main__':
    print(main())
