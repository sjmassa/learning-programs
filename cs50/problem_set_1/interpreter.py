

def main():
    user_input = input("Expression: ").split(' ')
    x = int(user_input[0])
    z = int(user_input[2])
    if user_input[1] == '+':
        print(f'{x + z:.1f}')
    elif user_input[1] == '-':
        print(f'{x - z:.1f}')
    elif user_input[1] == '*':
        print(f'{x * z:.1f}')
    elif user_input[1] == '/':
        print(f'{x / z:.1f}')

if __name__ == '__main__':
    main()
