def solution():
    """Emily loves to have pets and for that reason, she has 4 dogs in her home. Each one eats 250 grams of food per day. She has to go on vacation for 14 days. How many kilograms of food should she buy for her 4 dogs so they don't starve while she is out?"""
    dogs = 4
    food_per_dog = 0.25  # in kilograms
    days = 14
    total_food_needed = dogs * food_per_dog * days
    result = total_food_needed
    return result

print(solution())