def solution():
    # Calculate how much food the cat ate in 3 days
    food_eaten = 60 * 3 - 14

    # Calculate the weight of the food eaten in 3 days
    weight_eaten = food_eaten

    # Calculate the weight of the bowl before the cat ate
    bowl_weight = 420 - weight_eaten

    result = bowl_weight
    return result

print(solution())