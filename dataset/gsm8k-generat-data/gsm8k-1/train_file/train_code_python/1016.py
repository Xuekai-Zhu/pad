def solution():
    """Stacy has 2 more than triple as many berries as Steve. Steve has one half as many berries as Skylar. If Skylar has 20 berries, how many berries does Stacy have?"""
    skylar_berrie = 20
    steve_berrie = skylar_berrie / 2
    stacy_berrie = (3 * steve_berrie) + 2
    result = stacy_berrie
    return result

print(solution())