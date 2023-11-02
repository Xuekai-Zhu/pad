def solution():
    """John plays paintball 3 times a month. Each time he plays he buys 3 boxes of paintballs. They cost $25 per box. How much does he spend a month on paintballs?"""
    times_played = 3
    boxes_per_time = 3
    cost_per_box = 25
    total_cost = times_played * boxes_per_time * cost_per_box
    result = total_cost
    return result

print(solution())