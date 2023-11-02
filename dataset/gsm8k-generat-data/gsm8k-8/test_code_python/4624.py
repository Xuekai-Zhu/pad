def solution():
    # Calculate the total number of tractor-days worked
    tractor_days = (2 * 2) + (7 * 3)

    # Calculate the amount of acres per day needed for each tractor
    acres_per_day_per_tractor = 1700 / tractor_days

    result = acres_per_day_per_tractor
    return result

print(solution())