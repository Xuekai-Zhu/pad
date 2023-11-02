def solution():
    total_mushrooms = 32
    safe_mushrooms = 9

    # Calculate the number of poisonous mushrooms
    poisonous_mushrooms = (total_mushrooms - safe_mushrooms) * 2

    # Calculate the number of uncertain mushrooms
    uncertain_mushrooms = total_mushrooms - safe_mushrooms - poisonous_mushrooms
    result = uncertain_mushrooms
    return result

print(solution())