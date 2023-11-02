def solution():
    """John's pool is 5 feet deeper than 2 times Sarah’s pool. If John’s pool is 15 feet deep, how deep is Sarah’s pool?"""
    john_depth = 15
    sarah_depth = (john_depth - 5) / 2
    result = sarah_depth
    return result

print(solution())