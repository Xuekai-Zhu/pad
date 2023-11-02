def solution():
    num_goats = 4
    num_carrots = 47

    # Divide the number of carrots by the number of goats to find the number of carrots each goat gets
    carrots_per_goat = num_carrots // num_goats

    # Multiply the number of carrots each goat gets by the number of goats to find the total number of carrots used
    total_carrots_used = carrots_per_goat * num_goats

    # Subtract the total number of carrots used from the original number of carrots to find the number of carrots left over
    carrots_left_over = num_carrots - total_carrots_used
    result = carrots_left_over
    return result

print(solution())