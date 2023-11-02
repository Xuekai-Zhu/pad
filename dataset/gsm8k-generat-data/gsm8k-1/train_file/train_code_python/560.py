def solution():
    """Betty is 60 years old, and she is the oldest person in the family. Her daughter is 40 percent younger than she is, and her granddaughter is one-third her mother's age. How old is the granddaughter?"""
    betty_age = 60
    daughter_age = betty_age * 0.6
    granddaughter_age = daughter_age / 3
    result = granddaughter_age
    return result

print(solution())