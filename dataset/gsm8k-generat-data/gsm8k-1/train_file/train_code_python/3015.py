def solution():
    """Gary is buying chlorine for his rectangular pool, which is 10 feet long, 8 feet wide, and 6 feet deep. Gary needs to buy one quart of chlorine for every 120 cubic feet of water in his pool. If chlorine costs $3 a quart, how much does Gary spend on chlorine?"""
    pool_length = 10
    pool_width = 8
    pool_depth = 6
    pool_volume = pool_length * pool_width * pool_depth
    chlorine_ratio = 120
    chlorine_needed = pool_volume / chlorine_ratio
    chlorine_price = 3
    total_cost = chlorine_price * chlorine_needed
    result = total_cost
    return result

print(solution())