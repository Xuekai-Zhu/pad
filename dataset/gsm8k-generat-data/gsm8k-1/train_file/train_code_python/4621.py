def solution():
    """Annie went to a liquidation sale and bought 5 televisions that each cost $50. She also purchased 10 figurines. If Annie spent $260 in total, how much did a single figurine cost in dollars?"""
    tv_cost = 50
    num_tvs = 5
    total_tv_cost = tv_cost * num_tvs
    total_spent = 260
    figurine_cost = (total_spent - total_tv_cost) / 10
    result = figurine_cost
    return result

print(solution())