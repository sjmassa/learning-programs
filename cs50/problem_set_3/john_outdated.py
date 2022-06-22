

months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
    ]

# Converts alphabetical month to numerical
def month_to_number(user_month):
    x = 0
    for month in months:
        x += 1
        if user_month.lower() == month:
            user_month = x
            return user_month

# Accept a date from user and validates it against certain parameters
# Repeats until a valid date is given
def get_valid_date():
    while True:
        user_date = input("Date: ")
        slash_split = user_date.split('/')
        space_split = user_date.split(' ')
        # Tests if input is in mm/dd/yyyy numerical format
        # Then validates the date
        if len(slash_split) == 3:
            try:
                for element in slash_split:
                    int(element)
            except ValueError:
                continue
            if int(slash_split[0]) not in range(13):
                continue
            if int(slash_split[1]) not in range(32):
                continue
            if len(slash_split[2]) > 4:
                continue
            return slash_split
        # Tests if input is in MONTH DAY, YEAR format
        # Then validates the date
        elif len(space_split) == 3:
            space_split[1] = space_split[1].replace(',', '')
            try:
                for element in space_split[1:]:
                    int(element)
            except ValueError:
                continue
            if space_split[0].lower() in months:
                space_split[0] = month_to_number(space_split[0])
            else:
                continue
            if int(space_split[1]) not in range(32):
                continue
            if len(space_split[2]) > 4:
                continue
            return space_split

def main():
    date_list = get_valid_date()
    # Prints in YYYY-MM-DD format
    print(f"{int(date_list[2]):04d}-{int(date_list[0]):02d}-{int(date_list[1]):02d}")

if __name__ == "__main__":
    main()
