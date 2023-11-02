def solution():
    """John's pool is 5 feet deeper than 2 times Sarah’s pool. If John’s pool is 15 feet deep, how deep is Sarah’s pool?"""
    johns_pool_depth = 15
    sarahs_pool_depth = (johns_pool_depth - 5) / 2
    result = sarahs_pool_depth
    return result

print(solution())