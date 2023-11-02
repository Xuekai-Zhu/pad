def solution():
    """3 years ago James turned 27. In 5 years Matt will be twice James age. How old is Matt now?"""
    # Calculate James' current age
    james_age = 27 + 3 # James is currently 30 years old

    # Set up the equation for Matt's age
    # In 5 years, Matt will be twice James' age
    # m + 5 = 2(j + 5)
    # m + 5 = 2j + 10
    # m = 2j + 5 - 5
    # m = 2j
    # So Matt's current age is twice James' age minus 5
    matt_age = 2 * james_age - 5

    result = matt_age
    return result

print(solution())