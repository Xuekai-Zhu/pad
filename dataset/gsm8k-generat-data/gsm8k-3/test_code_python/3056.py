def solution():
    """My cat's empty bowl weighs 420 grams. If I give my cat 60 grams per day and I always fill her bowl every 3 days, how much does her bowl weigh if after I ended up refilling her empty bowl she only ate 14 grams?"""
    # Define the weight of the empty bowl and the amount of food given per day
    empty_bowl_weight = 420
    food_per_day = 60

    # Calculate the weight of the bowl after 3 days (before the cat eats)
    bowl_weight_after_3_days = empty_bowl_weight + (food_per_day * 3)

    # Calculate the weight of the bowl after the cat eats 14 grams
    bowl_weight_after_eating = bowl_weight_after_3_days - 14

    # Display the weight of the bowl after the cat eats
    result = bowl_weight_after_eating
    return result

print(solution())