def solution():
    """Timmy plans to ride a skateboard ramp that is 50 feet high. He knows he needs to go 40 mph at the start to make it all the way to the top. He measures his speed on three trial runs and goes 36, 34, and 38 mph. How much faster does he have to go than his average speed to make it up the ramp?"""
    desired_speed = 40
    ramp_height = 50
    trial_speeds = [36, 34, 38]
    average_speed = sum(trial_speeds) / len(trial_speeds)
    speed_difference = desired_speed - average_speed
    time_to_reach_ramp_top = ramp_height / desired_speed
    extra_speed_needed = ramp_height / time_to_reach_ramp_top - average_speed
    result = extra_speed_needed - speed_difference
    return result

print(solution())