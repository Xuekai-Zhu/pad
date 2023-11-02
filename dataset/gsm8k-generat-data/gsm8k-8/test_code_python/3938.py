def solution():
    # Calculate the total number of brownies
    total_brownies = 6 * 3

    # Subtract one brownie for Frank
    total_brownies -= 1

    # Divide the remaining brownies evenly among the 6 people
    brownies_per_person = total_brownies / 6
    result = brownies_per_person
    return result

print(solution())