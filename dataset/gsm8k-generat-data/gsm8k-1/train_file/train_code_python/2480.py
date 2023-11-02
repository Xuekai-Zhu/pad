def solution():
    """Mr. Wong harvested 560 mangoes from the tree outside his house. He sold half of it at the market and distributed the rest evenly among 8 of his neighbors. How many mangoes does each neighbor receive?"""
    mangoes_harvested = 560
    mangoes_sold = mangoes_harvested / 2
    mangoes_left = mangoes_harvested - mangoes_sold
    neighbors = 8
    mangoes_per_neighbor = mangoes_left / neighbors
    result = mangoes_per_neighbor
    return result

print(solution())