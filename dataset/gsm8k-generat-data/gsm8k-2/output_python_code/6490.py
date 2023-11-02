def solution():
    """James gets a cable program. The first 100 channels cost $100 and the next 100 channels cost half that much. He splits it evenly with his roommate. How much did he pay?"""
    first_100_cost = 100
    next_100_cost = first_100_cost / 2
    total_channels = 200
    james_share = (first_100_cost + next_100_cost * 100) / 2
    result = james_share
    return result

print(solution())