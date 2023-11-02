def solution():
    """At 30, Anika is 4/3 the age of Maddie. What would be their average age in 15 years?"""
    anika_age = 30
    maddie_age = (4/3) * anika_age
    average_age_in_15_years = (anika_age + 15 + maddie_age + 15) / 2
    result = average_age_in_15_years
    return result

print(solution())