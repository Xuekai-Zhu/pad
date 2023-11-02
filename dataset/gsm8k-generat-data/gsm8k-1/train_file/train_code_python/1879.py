def solution():
    """Milo can roll downhill on his skateboard at twice the speed that he can run. And Milo's best friend, Cory, can drive his wheelchair at twice the speed that Milo can roll downhill on his skateboard. If Cory always drives his wheelchair at 12 miles per hour, how many miles can Milo run in two hours?"""
    cory_speed = 12
    milo_skateboard_speed = cory_speed / 2
    milo_running_speed = milo_skateboard_speed / 2
    running_time = 2  # in hours
    distance_covered = milo_running_speed * running_time
    result = distance_covered
    return result

print(solution())