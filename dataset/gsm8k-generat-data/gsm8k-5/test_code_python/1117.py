def solution():
    gladys_age = 30  # Gladys is 30 years old
    billy_age = gladys_age // 3  # Billy is 1/3 of Gladys' age
    lucas_age = (gladys_age - 2*billy_age) // 2  # Lucas' age can be calculated using Gladys and Billy's age

    lucas_age_in_3_years = lucas_age + 3  # Add 3 years to Lucas' current age

    result = lucas_age_in_3_years
    return result

print(solution())