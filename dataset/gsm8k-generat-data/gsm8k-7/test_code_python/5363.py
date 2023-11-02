def solution():
    goal_liters = 3
    ml_per_drink = 500
    time_between_drinks = 2  # in hours

    # Convert the goal liters to milliliters
    goal_ml = goal_liters * 1000

    # Calculate how many milliliters Sandy can drink in one day
    ml_per_day = 0
    hours = 0
    while ml_per_day < goal_ml:
        ml_per_day += ml_per_drink
        hours += time_between_drinks

    result = hours
    return result

print(solution())