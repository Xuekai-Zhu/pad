def solution():
    """The pirates plan to explore 4 islands. Two islands require walking 20 miles per day while the other two islands require 25 miles per day. How many miles will they have to walk if it takes 1.5 days to explore each island?"""
    island1_distance = 20 * 1.5
    island2_distance = 20 * 1.5
    island3_distance = 25 * 1.5
    island4_distance = 25 * 1.5
    total_distance = island1_distance + island2_distance + island3_distance + island4_distance
    result = total_distance
    return result

print(solution())