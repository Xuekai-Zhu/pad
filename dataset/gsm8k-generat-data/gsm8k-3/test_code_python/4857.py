def solution():
    """There are six peregrine falcons and 40 pigeons nesting in Malcolm's skyscraper. Each pigeon has 6 chicks. If the peregrines eat 30% of the pigeons, how many pigeons are left?"""
    # Calculate the total number of chicks
    total_chicks = 40 * 6

    # Calculate the number of pigeons eaten by the falcons
    pigeons_eaten = 0.3 * 40

    # Calculate the number of pigeons left
    pigeons_left = 40 - pigeons_eaten

    # Display the number of pigeons left
    result = pigeons_left
    return result

print(solution())