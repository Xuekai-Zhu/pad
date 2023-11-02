def solution():
    tea_per_day = 1/5  # Marco uses a fifth of an ounce of tea leaves each day
    tea_per_box = 28  # Marco buys tea leaves in boxes of 28 ounces
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total amount of tea Marco gets from a box
    total_tea = tea_per_box / tea_per_day

    # Calculate the number of weeks of daily tea Marco gets from a box
    weeks_of_tea = total_tea / days_per_week
    result = weeks_of_tea
    return result

print(solution())