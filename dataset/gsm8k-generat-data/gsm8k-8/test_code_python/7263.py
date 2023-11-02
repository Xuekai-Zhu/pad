def solution():
    # Define the number of kittens and adult cats
    num_kittens = 4
    num_adult_cats = 3

    # Define the amount of food each cat needs per day
    food_per_adult_cat = 1
    food_per_kitten = 3/4

    # Calculate the total amount of food needed for 7 days
    total_food_needed = 7 * ((num_kittens * food_per_kitten) + (num_adult_cats * food_per_adult_cat))

    # Calculate the additional cans of food needed
    additional_food_needed = total_food_needed - 7

    result = additional_food_needed
    return result

print(solution())