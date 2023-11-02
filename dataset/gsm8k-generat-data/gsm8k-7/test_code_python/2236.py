def solution():
    shells_per_day = 10
    num_days = 6
    shells_given_to_brother = 2

    # Calculate the total number of shells collected
    total_shells_collected = shells_per_day * num_days

    # Calculate the number of shells left after giving some to her brother
    shells_left = total_shells_collected - shells_given_to_brother
    result = shells_left
    return result

print(solution())