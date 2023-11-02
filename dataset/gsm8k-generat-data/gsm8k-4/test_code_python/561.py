def solution():
    """Betty is 60 years old, and she is the oldest person in the family. Her daughter is 40 percent younger than she is, and her granddaughter is one-third her mother's age. How old is the granddaughter?"""
    # Define Betty's age
    betty_age = 60

    # Calculate Betty's daughter's age
    daughter_age = betty_age * 0.6

    # Calculate the granddaughter's age
    granddaughter_age = daughter_age / 3

    result = granddaughter_age
    return result

print(solution())