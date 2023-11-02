def solution():
    shells_per_day = 10  # Evie collects 10 shells per day
    days = 6  # Evie collects shells for 6 days

    # Calculate the total number of shells Evie collects
    total_shells = shells_per_day * days

    # Subtract the two shells she gives to her brother
    shells_left = total_shells - 2
    result = shells_left
    return result

print(solution())