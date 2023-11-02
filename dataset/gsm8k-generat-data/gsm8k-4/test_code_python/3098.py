def solution():
    """The ages of three brothers are consecutive integers with the sum of 96. How old is the youngest brother?"""
    # Define the sum of the ages of the three brothers
    total_age = 96

    # Set up the equation to find the youngest brother's age
    # Let x be the age of the youngest brother
    # Then the ages of the other two brothers are x+1 and x+2
    equation = x + (x + 1) + (x + 2) == total_age

    # Solve the equation for x
    x = (total_age - 3) / 3

    # Round down to get the youngest brother's age
    youngest_brother_age = int(x)

    # return the result
    result = youngest_brother_age
    return result

print(solution())