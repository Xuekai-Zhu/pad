def solution():
    # Define Eustace's current age
    eustace_current_age = 39 - 3

    # Define the ratio of Eustace's age to Milford's age
    eustace_to_milford_ratio = 2

    # Calculate Milford's current age
    milford_current_age = eustace_current_age / eustace_to_milford_ratio

    # Calculate Milford's age in 3 years
    milford_age_in_3_years = milford_current_age + 3
    result = milford_age_in_3_years
    return result

print(solution())