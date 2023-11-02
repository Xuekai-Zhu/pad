def solution():
    router_time = 10
    hold_time = 6 * router_time
    yell_time = hold_time / 2

    # Calculate the total time spent on all activities
    total_time = router_time + hold_time + yell_time
    result = total_time
    return result

print(solution())