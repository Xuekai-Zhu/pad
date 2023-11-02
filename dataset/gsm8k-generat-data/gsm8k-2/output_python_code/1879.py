def solution():
    """Milo can roll downhill on his skateboard at twice the speed that he can run. And Milo's best friend, Cory, can drive his wheelchair at twice the speed that Milo can roll downhill on his skateboard. If Cory always drives his wheelchair at 12 miles per hour, how many miles can Milo run in two hours?"""
    milo_skateboard_speed = 2 * milo_running_speed
    cory_wheelchair_speed = 2 * milo_skateboard_speed
    milo_time_running = 2
    milo_distance_running = milo_running_speed * milo_time_running
    result = milo_distance_running
    return result

print(solution())