def solution():
    """On a particular week, a tow truck pulled ten cars for each of the first three days and then four fewer cars on each of the remaining days of the week. Calculate the total number of cars it towed that week."""
    cars_towed_first_three_days = 10 * 3
    cars_towed_remaining_days = sum(range(10, 2, -4))
    total_cars_towed = cars_towed_first_three_days + cars_towed_remaining_days
    result = total_cars_towed
    return result

print(solution())