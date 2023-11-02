def solution():
    # Calculate the age of Betty's daughter
    daughter_age = 0.6 * 60 * 0.6  # Betty's daughter is 40% younger than she is
    # Calculate the age of Betty's granddaughter
    granddaughter_age = daughter_age / 3  # Betty's granddaughter is one-third her mother's age
    result = granddaughter_age
    return result

print(solution())