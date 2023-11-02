def solution():
    # Define the number of goats and the number of baby carrots
    num_goats = 4
    num_carrots = 47

    # Calculate the number of carrots each goat gets
    carrots_per_goat = num_carrots // num_goats

    # Calculate the remaining carrots
    remaining_carrots = num_carrots % num_goats

    result = remaining_carrots
    return result

print(solution())