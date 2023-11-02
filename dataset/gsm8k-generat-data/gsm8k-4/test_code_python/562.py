def solution():
    """Joy fosters dogs. The mom foster dog eats 1.5 cups of food, three times a day. The puppies each eat 1/2 cup of food, twice a day. There are 5 puppies. How much food will Joy need for the next 6 days?"""
    # Define the amount of food needed per dog per meal
    mom_dog_food = 1.5
    puppy_food = 0.5

    # Define the number of meals per day
    mom_dog_meals = 3
    puppy_meals = 2

    # Define the number of days
    days = 6

    # Calculate the total amount of food needed for the mom dog per day
    mom_dog_food_per_day = mom_dog_food * mom_dog_meals

    # Calculate the total amount of food needed for all the puppies per day
    puppies_food_per_day = puppy_food * puppy_meals * 5

    # Calculate the total amount of food needed per day
    total_food_per_day = mom_dog_food_per_day + puppies_food_per_day

    # Calculate the total amount of food needed for the next 6 days
    total_food_needed = total_food_per_day * days

    result = total_food_needed
    return result

print(solution())