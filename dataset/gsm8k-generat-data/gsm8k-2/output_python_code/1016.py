def solution():
    """Stacy has 2 more than triple as many berries as Steve. Steve has one half as many berries as Skylar. If Skylar has 20 berries, how many berries does Stacy have?"""
    skylar_berries = 20
    steve_berries = skylar_berries / 2
    stacy_berries = 3 * steve_berries + 2
    result = stacy_berries
    return result

print(solution())