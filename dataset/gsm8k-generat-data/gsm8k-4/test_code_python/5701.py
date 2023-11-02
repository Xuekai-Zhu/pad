def solution():
    """Alvin is 30 years old and Simon is 5 years away from being 1/2 the age of Alvin. How old is Simon?"""
    # Define Alvin's age
    alvin_age = 30

    # Calculate the age when Simon will be 1/2 of Alvin's age
    simon_half_age = alvin_age * 0.5 - 5

    # Calculate Simon's current age
    simon_age = simon_half_age + 5

    result = simon_age
    return result

print(solution())