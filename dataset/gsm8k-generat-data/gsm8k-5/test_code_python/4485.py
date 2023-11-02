def solution():
    ice_cream_melting_time = 10 / 60  # Convert 10 minutes to hours
    beach_distance = 16 * (1/8)  # Convert 16 blocks to miles
    time_to_reach_beach = beach_distance / desired_speed

    # Calculate the speed Jack needs to jog in order to reach the beach before the ice cream melts
    desired_speed = beach_distance / (time_to_reach_beach + ice_cream_melting_time)
    result = desired_speed
    return result

print(solution())