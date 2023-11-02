def solution():
    """Jason's stove catches on fire. Buying a replacement will cost $1200 and fixing the damage to the wall behind it will cost 1/6th as much. How much does he spend in total?"""
    stove_cost = 1200
    wall_cost = stove_cost / 6
    total_cost = stove_cost + wall_cost
    result = total_cost
    return result

print(solution())