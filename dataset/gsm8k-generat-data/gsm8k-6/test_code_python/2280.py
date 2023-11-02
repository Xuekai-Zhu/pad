def solution():
    initial_length = 20  # meters
    length_given_to_Allan = initial_length * (1/4)
    length_remaining = initial_length - length_given_to_Allan
    length_given_to_Jack = length_remaining * (2/3)
    length_remaining = length_remaining - length_given_to_Jack
    result = length_remaining
    return result

print(solution())