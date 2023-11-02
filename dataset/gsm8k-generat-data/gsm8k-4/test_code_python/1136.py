def solution():
    """Emily loves to have pets and for that reason, she has 4 dogs in her home. Each one eats 250 grams of food per day. She has to go on vacation for 14 days. How many kilograms of food should she buy for her 4 dogs so they don't starve while she is out?"""
    # Define the number of dogs and the amount of food each one eats
    num_dogs = 4
    food_per_dog = 250/1000 # convert grams to kilograms

    # Calculate the total amount of food needed for 14 days
    total_food = num_dogs * food_per_dog * 14

    # Round up to the nearest hundredth
    total_food = round(total_food, 2)

    # Return the result
    result = total_food
    return result

print(solution())