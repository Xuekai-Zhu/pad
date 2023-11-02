def solution():
    
    router_time = 10
    hold_time = 6 * router_time
    yelling_time = 0.5 * hold_time
    total_time = router_time + hold_time + yelling_time
    result = total_time
    return result

print(solution())