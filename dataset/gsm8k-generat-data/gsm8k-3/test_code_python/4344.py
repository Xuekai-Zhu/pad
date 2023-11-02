def solution():
    """Allie has 9 toys, which are in total worth $52. If we know that one toy is worth $12, and all the other toys have the same value, how much does one of the other toys cost?"""
    # Define the value of the known toy
    known_toy_value = 12

    # Determine the total value of the other toys
    other_toy_value = 52 - known_toy_value

    # Determine the number of other toys
    num_other_toys = 9 - 1

    # Determine the value of one of the other toys
    other_toy_cost = other_toy_value / num_other_toys

    # Display the cost of one of the other toys
    result = other_toy_cost
    return result

print(solution())