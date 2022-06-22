
#Take user input and convert with Einstein's famous equation.
def convert_kilograms(kilograms):
    m = int(kilograms)
    c = 300000000
    E = m*c**2
    return E

def main():
    user_input = input("Type a number, in kilograms, to be converted to joules: ")
    return convert_kilograms(user_input)

if __name__ == '__main__':
    print(main())
