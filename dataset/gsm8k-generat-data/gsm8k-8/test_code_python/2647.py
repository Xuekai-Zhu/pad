def solution():
    # Calculate the number of pythons in the park
    pythons = 3 * 40

    # Calculate the total number of non-rattlesnake snakes
    non_rattlesnakes = pythons + 40

    # Calculate the number of rattlesnakes in the park
    rattlesnakes = 200 - non_rattlesnakes

    result = rattlesnakes
    return result

print(solution())