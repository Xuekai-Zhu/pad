def solution():
    ramp_height = 50
    required_speed = 40
    speeds = [36, 34, 38]

    # Calculate the average speed of the trial runs
    avg_speed = sum(speeds) / len(speeds)

    # Calculate the speed difference needed to reach the required speed
    difference = required_speed - avg_speed

    # Calculate the height Timmy can reach with his average speed
    max_height = (avg_speed ** 2) / (2 * 32.2)

    # Calculate the height difference to reach the top of the ramp
    height_difference = ramp_height - max_height

    # Calculate the speed needed to reach the top of the ramp
    required_speed = (2 * 32.2 * height_difference) ** 0.5

    # Calculate the speed difference needed to reach the required speed to reach the top of the ramp
    speed_difference = required_speed - avg_speed

    result = speed_difference
    return result

print(solution())