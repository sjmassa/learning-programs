
#Take user input and iterate through the string to convert :) or :(.
def convert_faces(input_string):
    input_list = input_string.split()
    output_list = []
    for element in input_list:
        if element == ':)':
            element = '🙂'
        if element == ':(':
            element = '🙁'
        output_list += [element]
        output_string = ' '.join(output_list)
    return output_string

def main():
    user_input = input("Type something with a smiley or frowny: ")
    return convert_faces(user_input)

if __name__ == '__main__':
    print(main())
