def solution():
    # Calculate the total value of the 9 toys
    total_value = 52

    # Calculate the value of the one toy that we know the price of
    known_toy_value = 12

    # Calculate the total value of the other 8 toys
    other_toys_value = total_value - known_toy_value

    # Calculate the value of one of the other toys
    other_toy_value = other_toys_value / 8

    result = other_toy_value
    return result

print(solution())