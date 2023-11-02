def solution():
    empty_bowl_weight = 420  # Empty bowl weighs 420 grams
    food_per_day = 60  # Cat is given 60 grams of food per day
    refill_interval = 3  # Bowl is refilled every 3 days
    leftover_food = 14  # Cat only ate 14 grams after bowl was refilled

    # Calculate the weight of the food the cat eats in 3 days
    food_in_3_days = food_per_day * 3
    # Calculate the weight of the food the cat didn't eat in 3 days
    leftover_food_in_3_days = food_in_3_days - leftover_food
    # Calculate the weight of the food in the bowl when it's refilled
    bowl_weight_after_refill = empty_bowl_weight + leftover_food_in_3_days

    result = bowl_weight_after_refill
    return result

print(solution())