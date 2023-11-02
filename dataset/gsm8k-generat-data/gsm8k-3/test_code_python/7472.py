def solution():
    """At 30, Anika is 4/3 the age of Maddie. What would be their average age in 15 years?"""
    # Set up the equation for Anika's age in terms of Maddie's age
    # A = (4/3)M
    # At 30, A = 30
    # Solve for M
    Maddie_age = 30 * (3/4)

    # Calculate the ages of Anika and Maddie in 15 years
    Anika_future_age = 30 + 15
    Maddie_future_age = Maddie_age + 15

    # Calculate the average of their ages in 15 years
    average_age = (Anika_future_age + Maddie_future_age) / 2

    # Display the average age
    result = average_age
    return result

print(solution())