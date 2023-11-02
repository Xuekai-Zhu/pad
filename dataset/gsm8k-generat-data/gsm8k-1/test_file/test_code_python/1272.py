def solution():
    """James wants to hang crepe-paper streamers from his backyard fence for his birthday party. His backyard fence is a rectangle that measures 20 feet on the long side and 15 feet on the short side. How many feet of crepe paper does James need to buy?"""
    long_side = 20
    short_side = 15
    # perimeter of rectangle is sum of all sides
    perimeter = 2 * (long_side + short_side)
    result = perimeter
    
    return result

print(solution())