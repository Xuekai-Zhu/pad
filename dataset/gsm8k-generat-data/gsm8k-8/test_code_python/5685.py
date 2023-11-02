def solution():
    # Define Kilee's current age
    kilee_age = 20

    # Define the ratio of Cornelia's age to Kilee's age in 10 years
    cornelia_to_kilee_ratio = 3

    # Calculate Cornelia's age in 10 years
    cornelia_age_in_10_years = kilee_age * cornelia_to_kilee_ratio

    # Calculate Cornelia's current age
    cornelia_current_age = cornelia_age_in_10_years - 10
    result = cornelia_current_age
    return result

print(solution())