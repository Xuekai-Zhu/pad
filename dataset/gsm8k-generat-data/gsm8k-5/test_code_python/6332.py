def solution():
    total_mushrooms = 32  # Lillian found 32 mushrooms
    safe_mushrooms = 9  # Lillian identified 9 mushrooms as safe to eat
    poisonous_mushrooms = 2 * safe_mushrooms  # Lillian identified twice the amount she ate as poisonous
    uncertain_mushrooms = total_mushrooms - safe_mushrooms - poisonous_mushrooms  # Calculate the number of uncertain mushrooms

    result = uncertain_mushrooms
    return result

print(solution())