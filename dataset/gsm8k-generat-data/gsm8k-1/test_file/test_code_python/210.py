def solution():
    """Jerry has two pools, both with leaks emptying them out at 4 gallons/minute. 4 minutes ago, the big pool had twice as much water as the small pool. Now the big pool has four times as much water as the small pool. How much water does the small pool have now?"""
    leak_rate = 4
    time_passed = 4
    big_pool_ratio_four_min_ago = 2
    big_pool_ratio_now = 4
    
    # set up equations
    # let x be the amount of water in the small pool now
    # let y be the amount of water in the big pool now
    # x + y = initial_total_water
    # (y / 2) = big_pool_ratio_four_min_ago * (x / 2)
    # y = big_pool_ratio_now * x
    
    # solve for x
    # substitute y in terms of x from the third equation in the second equation
    # substitute y in terms of x from the third equation in the first equation
    # solve the resulting system of equations
    
    initial_total_water = big_pool_ratio_four_min_ago + 1
    x = (initial_total_water * leak_rate * time_passed) / (big_pool_ratio_now + big_pool_ratio_four_min_ago)
    result = x
    
    return result

print(solution())