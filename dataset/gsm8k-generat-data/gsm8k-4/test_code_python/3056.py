def solution():
    """My cat's empty bowl weighs 420 grams. If I give my cat 60 grams per day and I always fill her bowl every 3 days, how much does her bowl weigh if after I ended up refilling her empty bowl she only ate 14 grams?"""
    # Define the weight of an empty bowl and the amount of food given per day
    empty_bowl_weight = 420
    food_per_day = 60

    # Calculate the amount of food given every 3 days
    food_per_3_days = food_per_day * 3

    # Calculate the weight of the bowl after one 3-day period
    bowl_weight = empty_bowl_weight + food_per_3_days

    # Subtract the amount of food the cat actually ate from the bowl weight
    bowl_weight -= 14

    # Return the result
    result = bowl_weight
    return result

print(solution())