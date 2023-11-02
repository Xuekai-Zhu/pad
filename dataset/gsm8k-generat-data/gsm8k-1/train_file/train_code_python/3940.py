def solution():
    """Timmy plans to ride a skateboard ramp that is 50 feet high. He knows he needs to go 40 mph at the start to make it all the way to the top. He measures his speed on three trial runs and goes 36, 34, and 38 mph. How much faster does he have to go than his average speed to make it up the ramp?"""
    target_speed = 40
    ramp_height = 50
    trial_speeds = [36, 34, 38]
    average_speed = sum(trial_speeds) / len(trial_speeds)
    speed_difference = target_speed - average_speed
    time_to_top = ramp_height / target_speed
    distance_traveled = time_to_top * average_speed
    remaining_distance = ramp_height - distance_traveled
    needed_speed = remaining_distance / time_to_top
    speed_increase_needed = needed_speed - average_speed
    result = speed_increase_needed
    
    return result

print(solution())