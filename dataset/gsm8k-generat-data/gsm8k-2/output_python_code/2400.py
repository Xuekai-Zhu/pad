def solution():
    """A wild tiger escapes the zoo. He escapes at 1 AM and zookeepers do not notice he is missing until 4 AM. He runs at a speed of 25 mph. It takes 2 more hours to find him but after 4 hours of running, the tiger slows his speed to 10 mph. He then gets chased for half an hour going 50 mph. How far away from the zoo was he caught?"""
    escape_time = 3  # hours
    initial_speed = 25  # mph
    run_time_before_slowing = 4  # hours
    final_speed = 10  # mph
    chase_time = 0.5  # hours
    search_time = 2  # hours

    # Distance covered during the first run
    first_run_distance = (escape_time - run_time_before_slowing) * initial_speed

    # Distance covered during the slower run
    slower_run_distance = run_time_before_slowing * final_speed

    # Total distance covered before getting chased
    total_distance_before_chase = first_run_distance + slower_run_distance

    # Distance covered during the chase
    chase_distance = chase_time * 50

    # Total distance covered including the chase
    total_distance = total_distance_before_chase + chase_distance

    result = total_distance
    return result

print(solution())