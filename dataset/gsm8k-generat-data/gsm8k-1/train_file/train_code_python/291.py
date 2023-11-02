def solution():
    """May can knit 3 scarves using one yarn. She bought 2 red yarns, 6 blue yarns, and 4 yellow yarns. How many scarves will she be able to make in total?"""
    red_yarns = 2
    blue_yarns = 6
    yellow_yarns = 4
    scarves_per_yarn = 3
    total_scarves = (red_yarns + blue_yarns + yellow_yarns) * scarves_per_yarn
    result = total_scarves
    return result

print(solution())