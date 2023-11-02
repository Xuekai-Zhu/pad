def solution():
    pills_per_day = 1  # Joey takes 1 pill on the first day
    total_pills = pills_per_day  # initialize the total pills to the first day's pills

    # Calculate the pills taken each day for the next 6 days and add it to the total pills
    for i in range(2, 8):
        pills_per_day += 2  # Joey takes 2 more pills than the previous day
        total_pills += pills_per_day

    result = total_pills
    return result

print(solution())