

# User input in the form of X/Y
def get_input():
    while True:
        user_input = input("Fraction: ")
        user_input = user_input.partition('/')
        # Checks for non-numerical values
        # Checks for 0 division error
        try:
            x = float(user_input[0])
            y = float(user_input[2])
            x/y
        except (ValueError, ZeroDivisionError):
            continue
        if x > y:
            continue
        break
    return x, y
    

def main():
    x, y = get_input()
    percent = int((x/y)*100)
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{int(percent)}%")


if __name__ == "__main__":
    main()
