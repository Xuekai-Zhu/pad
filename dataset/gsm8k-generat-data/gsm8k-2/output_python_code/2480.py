def solution():
    """Mr. Wong harvested 560 mangoes from the tree outside his house. He sold half of it at the market and distributed the rest evenly among 8 of his neighbors. How many mangoes does each neighbor receive?"""
    total_mangoes = 560
    sold_mangoes = total_mangoes / 2
    remaining_mangoes = total_mangoes - sold_mangoes
    mangoes_per_neighbor = remaining_mangoes / 8
    result = mangoes_per_neighbor
    return result

print(solution())