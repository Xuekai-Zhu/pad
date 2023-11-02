def solution():
    """In 3 years, Jayden will be half of Ernesto's age. If Ernesto is 11 years old, how many years old is Jayden now?"""
    # Define Ernesto's current age
    ernesto_age = 11

    # Calculate how old Ernesto will be in 3 years
    ernesto_future_age = ernesto_age + 3

    # Calculate Jayden's current age based on Ernesto's future age
    jayden_age = (ernesto_future_age / 2) - 3

    # return the result
    result = jayden_age
    return result

print(solution())