def solution():
    """Monroe has a collection of ants and a collection of spiders. He has 8 spiders and 12 ants. He is wondering what the number of legs of the entire collection is."""
    spiders = 8
    ants = 12
    spider_legs = 8
    ant_legs = 6
    total_legs = (spiders * spider_legs) + (ants * ant_legs)
    result = total_legs
    return result

print(solution())