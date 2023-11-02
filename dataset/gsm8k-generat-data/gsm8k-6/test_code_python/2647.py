def solution():
    # Calculate the number of pythons
    num_pythons = 3 * 40  # three times as many pythons as boa constrictors

    # Calculate the number of rattlesnakes
    num_rattlesnakes = 200 - 40 - num_pythons  # the rest of the snakes are rattlesnakes

    result = num_rattlesnakes
    return result

print(solution())