def solution():
    """Viggo's age was 10 years more than twice his younger brother's age when his brother was 2. If his younger brother is currently 10 years old, what's the sum of theirs ages?"""
    # Calculate Viggo's age when his younger brother was 2
    viggo_age_at_2 = 2 * 2 + 10

    # Calculate the age difference between Viggo and his younger brother at that time
    age_difference = viggo_age_at_2 - 2

    # Calculate Viggo's current age
    viggo_age = age_difference + 10

    # Calculate the sum of their ages
    total_age = viggo_age + 10

    result = total_age
    return result

print(solution())