def solution():
    """Emily loves to have pets and for that reason, she has 4 dogs in her home. Each one eats 250 grams of food per day. She has to go on vacation for 14 days. How many kilograms of food should she buy for her 4 dogs so they don't starve while she is out?"""
    # Define the number of dogs and the amount of food they eat per day
    NUM_DOGS = 4
    FOOD_PER_DAY = 250 # in grams

    # Define the number of days Emily will be on vacation
    NUM_DAYS = 14

    # Calculate the total amount of food needed for all the dogs
    total_food = NUM_DOGS * FOOD_PER_DAY * NUM_DAYS # in grams

    # Convert the total amount of food to kilograms
    total_food_kg = total_food / 1000

    # Display the total amount of food needed in kilograms
    result = total_food_kg
    return result

print(solution())