def solution():
    """At 30, Anika is 4/3 the age of Maddie. What would be their average age in 15 years?"""
    # Define Anika's current age and the ratio of her age to Maddie's age
    anika_age = 30
    anika_maddie_ratio = 4/3

    # Calculate Maddie's current age
    maddie_age = anika_age / anika_maddie_ratio

    # Calculate the sum of their ages in 15 years
    sum_ages = (anika_age + 15) + (maddie_age + 15)

    # Calculate their average age in 15 years
    avg_age = sum_ages / 2

    result = avg_age
    return result

print(solution())