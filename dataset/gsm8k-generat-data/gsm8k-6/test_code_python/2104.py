def solution():
    # Calculate the total time Bill spends preparing for and cooking the omelets
    chopping_time = (3 * 4) + (4 * 2)  # it takes 3 minutes to chop a pepper and 4 minutes to chop an onion
    grating_time = 1 * 5 * 5  # it takes 1 minute to grate cheese for one omelet and he's making 5 omelets
    cooking_time = 5 * 5  # it takes 5 minutes to cook one omelet and he's making 5 omelets
    total_time = chopping_time + grating_time + cooking_time
    result = total_time
    return result

print(solution())