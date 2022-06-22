
#Takes a sentence from a user and converts all spaces to '...'.
def space_to_dots():
    string = input("Type a sentence: ")
    string = string.split()
    return "...".join(string)

def main():
    return space_to_dots()

if __name__ == '__main__':
    print(main())
