def solution():
    """Zion is 8 years old and his dad is 3 more than 4 times his age. In 10 years, how many years older is Zion's dad than him?"""
    zion_age = 8
    dad_age = 4*zion_age + 3
    diff_in_ages = dad_age - zion_age
    age_in_10_years = diff_in_ages + 10
    result = age_in_10_years
    return result

print(solution())