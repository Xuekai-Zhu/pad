def solution():
    empty_bowl_weight = 420
    daily_food_amount = 60
    refill_frequency = 3
    amount_eaten = 14

    # Calculate the amount of food filled in the bowl every refill
    amount_filled = daily_food_amount * refill_frequency

    # Calculate the amount of food left in the bowl after one refill
    amount_left = amount_filled - amount_eaten

    # Calculate the weight of the bowl with the remaining food
    bowl_weight = empty_bowl_weight + amount_left
    result = bowl_weight
    return result

print(solution())