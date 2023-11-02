def solution():
    bags_bought = 2  # Elise bought two bags of dog food
    weight_bought = 15 + 10  # Elise bought a 15kg bag and a 10kg bag

    # Calculate the total weight of dog food Elise now has
    total_weight = 40

    # Calculate the weight of dog food Elise already had
    weight_already_had = total_weight - weight_bought
    result = weight_already_had
    return result

print(solution())