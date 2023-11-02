def solution():
    """A wild tiger escapes the zoo. He escapes at 1 AM and zookeepers do not notice he is missing until 4 AM. He runs at a speed of 25 mph. It takes 2 more hours to find him but after 4 hours of running, the tiger slows his speed to 10 mph. He then gets chased for half an hour going 50 mph. How far away from the zoo was he caught?"""
    escape_time = 3  # 1 AM to 4 AM
    running_speed = 25
    running_time_before_slowing = 4
    running_speed_after_slowing = 10
    chasing_speed = 50
    chasing_time = 0.5
    distance_before_slowing = (escape_time + running_time_before_slowing) * running_speed
    distance_while_slowing = (running_speed_after_slowing * (escape_time + running_time_before_slowing + chasing_time))
    total_distance = distance_before_slowing + distance_while_slowing
    result = total_distance
    return result

print(solution())