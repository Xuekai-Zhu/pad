def solution():
    """Aunt Gemma has four dogs. She feeds them with dog food twice a day. Each dog can consume 250 grams of food per meal. If aunt Gemma bought 2 sacks of dog food, each weighing 50 kilograms, how many days will those food last?"""
    # Define the number of dogs and the amount of food they need per meal
    num_dogs = 4
    food_per_meal = 250  # in grams

    # Calculate the total amount of food the dogs need per day
    total_food_per_day = num_dogs * food_per_meal * 2  # in grams

    # Convert the total amount of food required per day to kilograms
    total_food_per_day = total_food_per_day / 1000  # in kilograms

    # Calculate the total amount of food in the two sacks
    total_food_in_sacks = 2 * 50  # in kilograms

    # Calculate how many days the food will last
    days_of_food = total_food_in_sacks / total_food_per_day

    # Display the number of days the food will last
    result = days_of_food
    return result

print(solution())