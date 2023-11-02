def solution():
    # Initialize variables
    time_spent = 5
    minute_multiplier = 2

    # Loop through remaining days and calculate time spent each day
    for i in range(2, 6):
        time_spent += (minute_multiplier ** (i-1)) * 5

    result = time_spent
    return result

print(solution())