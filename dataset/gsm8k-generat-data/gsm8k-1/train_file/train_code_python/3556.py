def solution():
    """Jim is a maintenance worker at a pool. Every time someone jumps in the pool, they cause 400 ml of water to splash out and evaporate.
    Jim has to get everyone out of the pool, clean, and refill it when it gets below 80% full.
    If the pool holds 2000 L of water, how many times can people jump in the pool before Jim has to clean it?"""
    pool_capacity = 2000   # L
    water_loss_per_jump = 0.4   # L
    water_to_clean = pool_capacity * (1 - 0.8)
    jumps_before_cleaning = water_to_clean / water_loss_per_jump
    result = int(jumps_before_cleaning)   # Round down to nearest integer jumps before cleaning
    
    return result

print(solution())