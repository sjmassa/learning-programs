
import sys

# A dictionary of fruit and corresponding calories
fruit_calories = {
    'apple': 130, 'avocado': 50, 'banana': 110,
    'cantaloupe': 50, 'grapefruit': 60, 'grapes': 90,
    'honeydew melon': 50, 'kiwifruit': 90, 'lemon': 15,
    'lime': 20, 'nectarine': 60, 'orange': 80, 'peach': 60,
    'pear': 100, 'pineapple': 50, 'plums': 70, 'strawberries': 50,
    'sweet cherries': 100, 'tangerine': 50, 'watermelon': 80
    }

# If user input fruit is in dictionary, return corresponding calories
# Otherwise exit script
def find_calories(fruit_calories, fruit):
    if fruit in fruit_calories:
        return f"Calories: {fruit_calories[fruit]}"
    sys.exit()

def main(fruit_calories):
    user_fruit = input("Type a fruit: ").lower()
    return find_calories(fruit_calories, user_fruit)

if __name__ == "__main__":
    print(main(fruit_calories))
