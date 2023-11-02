def solution():
    # Calculate the amount of supplies used on the first day
    day_1_usage = (2/5) * 400  

    # Calculate the remaining supplies after one day of sailing
    day_1_remaining = 400 - day_1_usage

    # Calculate the amount of supplies used on the next two days
    day_2_3_usage = (3/5) * day_1_remaining

    # Calculate the remaining supplies after the next two days of sailing
    remaining_supplies = day_1_remaining - day_2_3_usage

    result = remaining_supplies
    return result

print(solution())