def solution():
    """Justin is 26 years old. When he was born his elder sister Jessica was 6 years old. James is their elder brother and is 7 years older than Jessica. How old will James be after 5 years?"""
    # Calculate Jessica's current age
    jessica_age = 26 - 6

    # Calculate James's current age
    james_age = jessica_age + 7

    # Calculate James's age in 5 years
    james_age_in_5_years = james_age + 5

    # Display James's age in 5 years
    result = james_age_in_5_years
    return result

print(solution())