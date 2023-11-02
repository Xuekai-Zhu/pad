def solution():
    # Calculate the number of carrots each goat will get, assuming they get an equal amount
    num_goats = 4
    num_carrots_per_goat = 47 // num_goats  # integer division to ensure equal distribution

    # Calculate the number of leftover carrots
    leftover_carrots = 47 % num_goats

    result = leftover_carrots
    return result

print(solution())