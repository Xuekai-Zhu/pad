def solution():
    """In five years Sam will be 3 times as old as Drew. If Drew is currently 12 years old, how old is Sam?"""
    # Define Drew's current age
    drew_age = 12

    # Define the age difference in 5 years
    age_diff = 3 - 1  # (Sam will be 3 times as old as Drew in 5 years, so age difference is 2)

    # Calculate Sam's age in 5 years
    sam_age_5_years = drew_age * age_diff

    # Calculate Sam's current age
    sam_age = sam_age_5_years - 5

    # Display Sam's current age
    result = sam_age
    return result

print(solution())