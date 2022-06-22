

# Receive input from user for a camel case variable.
def user_variable():
    user_input = input("Type a camel case variable: ")
    return user_input

# Converts a variable from camel case to one with underscores.
def convert_variable(variable):
    converted_variable = ''
    for letter in variable:
        if letter.isupper():
            letter = "_"+letter.lower()
        converted_variable += letter
    return converted_variable

def main():
    user_input = user_variable()
    return convert_variable(user_input)

if __name__ == '__main__':
    print(main())
