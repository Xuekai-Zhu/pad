def solution():
    current_age_james = 27
    years_ago = 3
    future_years = 5

    # Calculate James' current age
    current_year = 2021
    birth_year = current_year - years_ago - current_age_james
    current_age_james = current_year - birth_year

    # Calculate James' age in 5 years
    future_age_james = current_age_james + future_years

    # Calculate Matt's age in 5 years
    future_age_matt = 2 * future_age_james

    # Calculate Matt's current age
    current_age_matt = future_age_matt - future_years
    result = current_age_matt
    return result

print(solution())