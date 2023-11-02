def solution():
    # Set Lennon's current age and the number of years in the future
    lennon_age = 8
    future_years = 2

    # Calculate Ophelia's age in the future using the given ratio
    future_ophelia_age = (lennon_age + future_years) * 4

    # Calculate Ophelia's current age by subtracting the number of future years
    ophelia_age = future_ophelia_age - future_years
    result = ophelia_age
    return result

print(solution())