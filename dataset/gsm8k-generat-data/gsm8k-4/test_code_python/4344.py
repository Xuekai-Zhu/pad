def solution():
    """Allie has 9 toys, which are in total worth $52. If we know that one toy is worth $12, and all the other toys have the same value, how much does one of the other toys cost?"""
    # Define the value of one of the toys
    one_toy_value = 12

    # Calculate the total value of the 9 toys
    total_value = 52

    # Subtract the value of the known toy from the total value to find the value of the remaining 8 toys
    remaining_value = total_value - one_toy_value

    # Divide the remaining value by the number of remaining toys to find the value of one of the other toys
    other_toy_value = remaining_value / 8

    result = other_toy_value
    return result

print(solution())