def solution():
    # Find Eustace's current age
    eustace_age = 39 - 3  # In 3 years Eustace will be 39
    # Find Milford's current age
    milford_age = eustace_age / 2  # Eustace is twice as old as Milford
    # Find Milford's age in 3 years
    milford_age_in_3_years = milford_age + 3
    result = milford_age_in_3_years
    return result

print(solution())