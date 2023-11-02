def solution():
    """Mr. Wong harvested 560 mangoes from the tree outside his house. He sold half of it at the market and distributed the rest evenly among 8 of his neighbors. How many mangoes does each neighbor receive?"""
    # Define the number of mangoes harvested
    total_mangoes = 560

    # Calculate the number of mangoes sold at the market
    market_mangoes = total_mangoes / 2

    # Calculate the number of mangoes remaining
    remaining_mangoes = total_mangoes - market_mangoes

    # Calculate the number of mangoes each neighbor receives
    neighbor_mangoes = remaining_mangoes / 8

    # Return the result
    result = neighbor_mangoes
    return result

print(solution())