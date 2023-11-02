def solution():
    """Justin is 26 years old. When he was born his elder sister Jessica was 6 years old. James is their elder brother and is 7 years older than Jessica. How old will James be after 5 years?"""
    # Define Justin's age
    justins_age = 26

    # Define Jessica's age when Justin was born
    jessicas_age_at_justins_birth = 6

    # Calculate Jessica's current age
    jessicas_age = justins_age + jessicas_age_at_justins_birth

    # Calculate James' age
    james_age = jessicas_age + 7

    # Calculate James' age in 5 years
    james_age_in_5_years = james_age + 5

    result = james_age_in_5_years
    return result

print(solution())