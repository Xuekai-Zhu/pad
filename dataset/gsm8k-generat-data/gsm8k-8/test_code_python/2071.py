def solution():
    # Define the time for one minute and the length of one push-up set
    time = 60
    set_length = 10 + 8 + 8

    # Calculate the number of sets Jackie can complete in one minute
    sets_per_minute = time // set_length

    # Calculate the total number of push-ups Jackie can do in one minute
    pushups_per_set = 5
    total_pushups = sets_per_minute * pushups_per_set

    result = total_pushups
    return result

print(solution())