def solution():
    # Calculate Gervais' total distance driven
    gervais_distance = 315 * 3

    # Calculate Henri's average daily distance driven
    henri_daily_distance = 1250 / 7

    # Calculate Henri's total distance driven in the same 3 days as Gervais
    henri_distance = henri_daily_distance * 3

    # Calculate how many miles farther Henri drove than Gervais
    miles_farther = henri_distance - gervais_distance
    result = miles_farther
    return result

print(solution())