
def main():
    while True:
        user_input = input("What time is it? ").split(':')
        if int(user_input[0]) < 0 or int(user_input[0]) > 24:
            print("Invalid input")
        else:
            break
    convert(user_input)


def convert(time):
    if int(time[0]) == 7 and int(time[1]) <= 59:
        print("breakfast time")
    elif int(time[0]) == 12 and int(time[1]) <= 59:
        print("lunch time")
    elif int(time[0]) == 18 and int(time[1]) <= 59:
        print("dinner time")

if __name__ == "__main__":
    main()
