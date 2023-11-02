def solution():
    # Define Cori's current age and the number of years in the future
    cori_age = 3
    future_years = 5

    # Calculate Cori's age in the future
    cori_future_age = cori_age + future_years

    # Calculate her aunt's age in the future
    aunt_future_age = cori_future_age * 3

    # Calculate her aunt's current age
    aunt_current_age = aunt_future_age - future_years
    result = aunt_current_age
    return result

print(solution())