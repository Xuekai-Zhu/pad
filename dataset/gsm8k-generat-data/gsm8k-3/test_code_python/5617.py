def solution():
    """How long is it before Kayla can reach the minimum age of driving of her state, which is 18, if she is currently half the age of her sister Kimiko who is 26 years old?"""
    # Define Kimiko's age
    kimiko_age = 26

    # Calculate Kayla's age
    kayla_age = kimiko_age / 2

    # Calculate the number of years until Kayla reaches the minimum driving age
    years_until_driving_age = 18 - kayla_age

    # Display the number of years
    result = years_until_driving_age
    return result

print(solution())