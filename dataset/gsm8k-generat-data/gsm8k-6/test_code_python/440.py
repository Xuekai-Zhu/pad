def solution():
    cori_age = 3  # Cori's current age
    aunt_age_in_5_years = 3 * (cori_age + 5)  # Cori will be one-third her aunt's age in 5 years
    aunt_age = aunt_age_in_5_years - 5  # Subtract 5 years to get aunt's current age
    result = aunt_age
    return result

print(solution())