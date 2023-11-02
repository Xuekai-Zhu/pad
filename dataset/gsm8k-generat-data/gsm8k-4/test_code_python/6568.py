def solution():
    """Aunt Gemma has four dogs. She feeds them with dog food twice a day. Each dog can consume 250 grams of food per meal. If aunt Gemma bought 2 sacks of dog food, each weighing 50 kilograms, how many days will those food last?"""
    # Define the number of dogs and the amount of food they consume
    num_dogs = 4
    food_per_dog = 0.25 # in kilograms

    # Define the amount of food in the sacks
    food_per_sack = 50 # in kilograms
    total_food = food_per_sack * 2 # in kilograms

    # Calculate the total amount of food needed per day
    total_daily_food = num_dogs * food_per_dog * 2 # in kilograms

    # Calculate the number of days the food will last
    days = total_food / total_daily_food

    result = round(days)
    return result

print(solution())