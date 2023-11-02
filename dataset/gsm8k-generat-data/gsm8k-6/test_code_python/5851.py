def solution():
    # Calculate the number of crickets Gilbert eats per week
    temp_90 = 0.8 * 15  # number of weeks when the temperature is 90 degrees F
    temp_100 = 0.2 * 15  # number of weeks when the temperature is 100 degrees F
    crickets_90 = 4 * temp_90  # number of crickets Gilbert eats per week when the temp is 90 degrees F
    crickets_100 = 8 * temp_100  # number of crickets Gilbert eats per week when the temp is 100 degrees F
    total_crickets = crickets_90 + crickets_100  # total number of crickets Gilbert eats over 15 weeks
    result = total_crickets
    return result

print(solution())