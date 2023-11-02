def solution():
    """How long is it before Kayla can reach the minimum age of driving of her state, which is 18, if she is currently half the age of her sister Kimiko who is 26 years old?"""
    # Calculate the age of Kayla
    kayla_age = 26 / 2

    # Calculate the number of years until Kayla reaches the minimum driving age of 18
    years_until_driving_age = 18 - kayla_age

    # Return the result
    result = years_until_driving_age
    return result

print(solution())