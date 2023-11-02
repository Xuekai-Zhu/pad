def solution():
    """Viggo's age was 10 years more than twice his younger brother's age when his brother was 2. If his younger brother is currently 10 years old, what's the sum of theirs ages?"""
    # Calculate Viggo's age when his brother was 2
    viggo_age_at_2 = 10 + 2 * 2  # 10 years more than twice his brother's age

    # Calculate Viggo's current age
    viggo_age_now = viggo_age_at_2 + (10 - 2)  # add the age difference between then and now

    # Calculate the sum of their ages
    total_age = viggo_age_now + 10  # add Viggo's age and his brother's current age

    # Display the total age
    result = total_age
    return result

print(solution())