def solution():
    """When you take Hiram's age and then add 12, you get 4 less than twice Allyson's age. If Hiram is 40 years old, how old is Allyson?"""
    # Define Hiram's age
    hiram_age = 40

    # Calculate twice Allyson's age
    twice_allyson_age = (hiram_age + 12 + 4) * 0.5

    # Calculate Allyson's age
    allyson_age = (twice_allyson_age - 4)

    result = allyson_age
    return result

print(solution())