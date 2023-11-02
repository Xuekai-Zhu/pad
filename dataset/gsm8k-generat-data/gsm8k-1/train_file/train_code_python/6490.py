def solution():
    """James gets a cable program. The first 100 channels cost $100 and the next 100 channels cost half that much. He splits it evenly with his roommate. How much did he pay?"""
    cost_first_100 = 100
    cost_next_100 = cost_first_100 / 2
    total_cost = cost_first_100 + cost_next_100
    james_share = total_cost / 2
    result = james_share
    return result

print(solution())