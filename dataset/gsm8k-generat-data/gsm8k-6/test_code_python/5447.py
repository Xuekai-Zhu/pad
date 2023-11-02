def solution():
    # Calculate the time it takes to heat the water to boiling point
    water_temp = 41
    time_to_boil = (212 - water_temp) / 3  # the temperature increases by 3 degrees every minute

    # Calculate the total time for cooking pasta, mixing with sauce, and making salad
    pasta_time = 12
    total_time = pasta_time + (1/3) * pasta_time + time_to_boil

    result = total_time
    return result

print(solution())