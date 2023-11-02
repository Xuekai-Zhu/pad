def solution():
    required_speed = 40  # Timmy needs to go 40 mph at the start to make it all the way to the top of the ramp
    measured_speeds = [36, 34, 38]  # Timmy measures his speed on three trial runs

    # Calculate the average of Timmy's measured speeds
    average_speed = sum(measured_speeds) / len(measured_speeds)

    # Calculate how much faster Timmy needs to go than his average speed to make it up the ramp
    difference = required_speed - average_speed
    result = difference
    return result

print(solution())