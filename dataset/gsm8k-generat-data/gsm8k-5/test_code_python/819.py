def solution():
    total_tins = 500  # James wants to collect 500 tins in a week
    tins_collected = 50 + (3 * 50) + (3 * 50 - 50)  # James collects 50 tins on day 1, 3 times that on day 2, and 50 fewer than that on day 3
    remaining_days = 4  # James has 4 days left to collect tins

    # Calculate the average number of tins James needs to collect each day for the rest of the week
    average_tins_per_day = (total_tins - tins_collected) / remaining_days
    result = average_tins_per_day
    return result

print(solution())