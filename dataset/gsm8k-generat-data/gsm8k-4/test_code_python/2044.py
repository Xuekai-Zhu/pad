def solution():
    """Twenty years ago, Shane was 2 times older than Garret is now. If Garret is currently 12, how old is Shane now?"""
    # Define Garret's current age
    garret_age = 12

    # Calculate Shane's age 20 years ago
    shane_age_20_years_ago = garret_age * 2

    # Calculate Shane's current age
    shane_age = shane_age_20_years_ago + 20

    result = shane_age
    return result

print(solution())