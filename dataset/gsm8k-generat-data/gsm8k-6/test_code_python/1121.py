def solution():
    # Determine Clara's age difference with Alice
    age_difference = 60 - (2/5)*60  # Clara has 2/5 times as many pens as Alice

    # Determine Clara's current age
    clara_age = 20 + age_difference

    # Calculate Clara's age in 5 years
    clara_age_in_5_years = clara_age + 5
    result = clara_age_in_5_years
    return result

print(solution())