def solution():
    # Define the total number of mushrooms Lillian found
    total_mushrooms = 32

    # Define the number of mushrooms Lillian can safely eat
    safe_mushrooms = 9

    # Define the number of mushrooms that are poisonous
    poisonous_mushrooms = 2 * safe_mushrooms

    # Define the number of mushrooms Lillian is uncertain about
    uncertain_mushrooms = total_mushrooms - safe_mushrooms - poisonous_mushrooms

    result = uncertain_mushrooms
    return result

print(solution())