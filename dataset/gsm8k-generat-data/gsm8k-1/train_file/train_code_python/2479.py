def solution():
    """A school choir needs robes for each of its 30 singers. Currently, the school has only 12 robes so they decided to buy the rest. If each robe costs $2, how much will the school spend?"""
    singers = 30
    current_robes = 12
    needed_robes = singers - current_robes
    cost_per_robe = 2
    total_cost = needed_robes * cost_per_robe
    result = total_cost
    
    return result

print(solution())