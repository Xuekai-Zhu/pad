def solution():
    """In five years Sam will be 3 times as old as Drew. If Drew is currently 12 years old, how old is Sam?"""
    # Define Drew's current age
    drew_age = 12

    # Calculate Sam's age in five years
    sam_age_5_years = drew_age * 3

    # Calculate Sam's current age
    sam_age = sam_age_5_years - 5

    # Return Sam's current age
    result = sam_age
    return result

print(solution())