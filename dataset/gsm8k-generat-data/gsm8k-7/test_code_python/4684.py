def solution():
    total_rain = 22
    second_hour_rain = 0
    first_hour_rain = 0

    # Use algebra to solve for the amount of rain in the first hour
    # Let x be the amount of rain in the first hour
    # Then, 7 + 2x is the amount of rain in the second hour
    # And, x + (7 + 2x) = 22 is the total amount of rain in the first two hours
    # Solving for x gives x = 5

    first_hour_rain = 5
    second_hour_rain = 7 + 2*first_hour_rain

    result = first_hour_rain
    return result

print(solution())