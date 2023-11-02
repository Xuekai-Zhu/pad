def solution():
    # Find Terry's age in 10 years
    terry_in_10_years = 4 * 10  # Terry will be 4 times Nora's age in 10 years
    
    # Find Terry's current age
    current_age_diff = terry_in_10_years - 10  # Terry's age will have increased by the same amount as Nora's current age
    current_age = current_age_diff + 10  # Add Nora's current age to the difference to find Terry's current age
    result = current_age
    return result

print(solution())