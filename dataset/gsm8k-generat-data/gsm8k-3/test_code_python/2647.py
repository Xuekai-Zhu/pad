def solution():
    """There are 200 snakes in a park. There are three times as many pythons as boa constrictors. If there 40 boa constrictors and the rest of the snakes are rattlesnakes, calculate the total number of rattlesnakes in the park."""
    # Calculate the total number of boa constrictors
    boa_constrictors = 40

    # Calculate the total number of pythons
    pythons = 3 * boa_constrictors

    # Calculate the total number of non-rattlesnakes
    non_rattlesnakes = boa_constrictors + pythons

    # Calculate the total number of rattlesnakes
    rattlesnakes = 200 - non_rattlesnakes

    # Display the total number of rattlesnakes
    result = rattlesnakes
    return result

print(solution())