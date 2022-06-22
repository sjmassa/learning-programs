

def input_string():
    user_string = input("Input: ")
    return user_string

# Removes vowels from a string
# Accounts for single character words that are vowels.
def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string_list = string.split()
    new_string_list = []
    for word in string_list:
        new_word = ''
        for letter in word:
            if letter.lower() not in vowels:
                new_word += letter
        if new_word != '':
            new_string_list += [new_word]
    converted_string = ' '.join(new_string_list)
    return converted_string

def main():
    user_string = input_string()
    removed_vowels_string = remove_vowels(user_string)
    return f"Output: {removed_vowels_string}"

if __name__ == "__main__":
    print(main())
