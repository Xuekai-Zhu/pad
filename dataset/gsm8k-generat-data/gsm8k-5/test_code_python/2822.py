def solution():
    age_difference = 10  # Jennifer will be 30 in 10 years
    sister_multiplier = 3  # Jordana will be 3 times as old as Jennifer in 10 years

    # Calculate Jennifer's age now
    jennifer_age = 30 - age_difference

    # Calculate Jordana's age in 10 years
    jordana_age_in_10_years = 30 + (sister_multiplier * age_difference)

    # Calculate Jordana's current age
    jordana_age = jordana_age_in_10_years - age_difference

    result = jordana_age
    return result

print(solution())