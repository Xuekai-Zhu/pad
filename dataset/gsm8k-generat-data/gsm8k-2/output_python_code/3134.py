def solution():
    """John is an eccentric millionaire. He decides to fill his swimming pool with bottled water. A cubic foot of water is 25 liters. His pool is 10 feet deep and 6 feet by 20 feet. A liter of water costs $3. How much does it cost to fill the pool?"""
    pool_depth = 10
    pool_width = 6
    pool_length = 20
    cubic_feet = pool_depth * pool_width * pool_length
    liters = cubic_feet * 25
    cost_per_liter = 3
    total_cost = liters * cost_per_liter
    result = total_cost
    return result

print(solution())