def solution():
    """Emily loves to have pets and for that reason, she has 4 dogs in her home. Each one eats 250 grams of food per day. She has to go on vacation for 14 days. How many kilograms of food should she buy for her 4 dogs so they don't starve while she is out?"""
    dogs = 4
    food_per_dog_per_day = 250
    days_on_vacation = 14
    total_food_needed = dogs * food_per_dog_per_day * days_on_vacation / 1000
    result = total_food_needed
    return result

print(solution())