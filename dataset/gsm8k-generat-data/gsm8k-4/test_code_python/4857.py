def solution():
    """There are six peregrine falcons and 40 pigeons nesting in Malcolm's skyscraper. Each pigeon has 6 chicks. If the peregrines eat 30% of the pigeons, how many pigeons are left?"""
    # Define the number of peregrine falcons and pigeons
    peregrine_falcons = 6
    pigeons = 40
    pigeon_chicks = pigeons * 6

    # Calculate the number of pigeons eaten by the falcons
    pigeons_eaten = pigeons * 0.3

    # Calculate the number of pigeons remaining
    pigeons_remaining = pigeons - pigeons_eaten

    result = pigeons_remaining
    return result

print(solution())