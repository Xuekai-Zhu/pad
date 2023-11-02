def solution():
    zion_age = 8
    dad_age = 3 + 4 * zion_age

    # In 10 years, Zion will be 18 years old and his dad will be (3 + 4*8) + 10 = 41 years old
    dad_age_after_10_years = dad_age + 10
    zion_age_after_10_years = zion_age + 10

    # Calculate the age difference between Zion's dad and him after 10 years
    age_difference = dad_age_after_10_years - zion_age_after_10_years
    result = age_difference
    return result

print(solution())