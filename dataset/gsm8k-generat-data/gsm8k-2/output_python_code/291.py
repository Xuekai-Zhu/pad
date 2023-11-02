def solution():
    """May can knit 3 scarves using one yarn. She bought 2 red yarns, 6 blue yarns, and 4 yellow yarns. How many scarves will she be able to make in total?"""
    scarves_per_yarn = 3
    total_red_yarns = 2
    total_blue_yarns = 6
    total_yellow_yarns = 4
    total_yarns = total_red_yarns + total_blue_yarns + total_yellow_yarns
    total_scarves = total_yarns * scarves_per_yarn
    result = total_scarves
    return result

print(solution())