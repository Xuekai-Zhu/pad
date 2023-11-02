def solution():
    # Calculate the total time Justin has been gathering flowers
    total_time = 2 * 60

    # Calculate the number of flowers Justin needs to collect
    num_flowers_needed = 30

    # Calculate the total time Justin needs to find all the flowers
    total_time_needed = num_flowers_needed * 10

    # Calculate the time Justin has already spent looking
    time_already_spent = total_time - 3 * 10

    # Calculate the remaining time Justin needs to look
    remaining_time = total_time_needed - time_already_spent

    result = remaining_time
    return result

print(solution())