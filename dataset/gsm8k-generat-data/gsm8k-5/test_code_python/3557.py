def solution():
    pool_capacity = 2000  # The pool can hold 2000 L of water
    water_loss_per_jump = 400  # Every time someone jumps in the pool, 400 ml of water splashes out and evaporates
    water_threshold = pool_capacity * 0.8  # Jim has to clean the pool when water level falls below 80% of the pool capacity

    # Calculate how many times people can jump in the pool before Jim has to clean it
    jumps_before_cleaning = int((pool_capacity - water_threshold) / water_loss_per_jump)
    result = jumps_before_cleaning
    return result

print(solution())