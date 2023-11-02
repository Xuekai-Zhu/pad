def solution():
    # Define the initial supplies and the fraction used on the first day
    initial_supplies = 400
    fraction_used_day1 = 2/5
    supplies_left_day1 = initial_supplies * (1 - fraction_used_day1)

    # Define the fraction used on the next two days
    fraction_used_day2 = 3/5
    fraction_used_day3 = 3/5

    # Calculate the supplies left after the next two days
    supplies_left_day3 = supplies_left_day1 * (1 - fraction_used_day2) * (1 - fraction_used_day3)

    result = supplies_left_day3
    return result

print(solution())