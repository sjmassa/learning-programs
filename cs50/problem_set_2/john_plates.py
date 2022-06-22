
# Checks user input against valid license plate naming rules
def is_valid(s):
    # Returns False if length of user input is less than 2 or greater than 6
    if len(s) < 2 or len(s) > 6:
        return False
    # Returns False if user input contains anything but letters and numbers
    if s.isalnum() is False:
        return False
    # Returns False if one of the first 2 characters is a number
    for letter in s[:2]:
        if letter.isnumeric():
            return False
    # Input can only end in a number and the first numeric digit cannot be a 0
    found_number = 0
    for char in s[2:]:
        if char.isnumeric():
            found_number += 1
        if char == '0' and found_number == 1:
            return False
        if char.isalpha() and found_number > 0:
            return False
    return True

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
