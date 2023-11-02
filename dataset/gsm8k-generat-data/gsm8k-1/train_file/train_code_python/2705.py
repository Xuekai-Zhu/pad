def solution():
    """A leaf is being blown down a sidewalk by swirling gusts of wind.For every five feet that a gust blows it forward, the wind swirls and blows it back two feet.How many feet has it traveled down the sidewalk after 11 gusts of wind?"""
    forward_distance = 5
    back_distance = 2
    net_distance = forward_distance - back_distance
    total_distance = net_distance * 11
    result = total_distance
    return result

print(solution())