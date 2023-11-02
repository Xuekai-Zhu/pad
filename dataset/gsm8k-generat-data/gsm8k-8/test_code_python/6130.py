def solution():
    # Define Audrey's and Heracles' ages
    audrey_age = heracles_age + 7

    # Set up the equation using algebra
    # a + 3 = 2h
    # a = h + 7
    # Substitute a with h + 7 and solve for h
    heracles_age = (3 - 7) / (2 - 1)

    # Round down to the nearest whole number since age cannot be a decimal
    heracles_age = int(heracles_age)

    result = heracles_age
    return result

print(solution())