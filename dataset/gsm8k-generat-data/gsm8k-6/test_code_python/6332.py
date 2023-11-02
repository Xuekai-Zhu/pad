def solution():
    # Calculate the number of poisonous mushrooms Lillian found
    poisonous_mushrooms = 2 * (32 - 9 - 1)  # Lillian had 9 safe mushrooms, identified one as uncertain, and the rest were poisonous

    # Calculate the number of uncertain mushrooms
    uncertain_mushrooms = 32 - 9 - poisonous_mushrooms - 1  # Lillian had 9 safe mushrooms, identified one as uncertain, and the rest were either poisonous or uncertain

    result = uncertain_mushrooms
    return result

print(solution())