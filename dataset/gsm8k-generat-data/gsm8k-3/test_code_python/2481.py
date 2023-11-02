def solution():
    """Mr. Wong harvested 560 mangoes from the tree outside his house. He sold half of it at the market and distributed the rest evenly among 8 of his neighbors. How many mangoes does each neighbor receive?"""
    # Calculate the number of mangoes Mr. Wong distributed
    mangoes_distributed = 560 / 2

    # Calculate the number of mangoes each neighbor received
    mangoes_per_neighbor = mangoes_distributed / 8

    # Display the number of mangoes each neighbor received
    result = mangoes_per_neighbor
    return result

print(solution())