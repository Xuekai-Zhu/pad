def solution():
    """James buys 3 dirt bikes for $150 each and 4 off-road vehicles for $300 each. It also cost him $25 to register each of these. How much did he pay for everything?"""
    dirt_bikes_cost = 150 * 3
    off_road_cost = 300 * 4
    registry_cost = 25 * 7
    total_cost = dirt_bikes_cost + off_road_cost + registry_cost
    result = total_cost
    return result

print(solution())