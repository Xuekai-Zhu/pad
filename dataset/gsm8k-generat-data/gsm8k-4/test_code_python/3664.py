def solution():
    """Bob's school track is 400 meters. If Bob ran the first lap in 70 seconds, the second and third lap in 85 seconds each, what was his average speed in (m/s) for his entire run?"""
    # Define the track distance
    track_distance = 400

    # Define the lap times
    lap1_time = 70
    lap2_time = 85
    lap3_time = 85

    # Calculate the total time for all 3 laps
    total_time = lap1_time + lap2_time + lap3_time

    # Calculate the average time per lap
    avg_time_per_lap = total_time / 3

    # Calculate the average speed
    avg_speed = track_distance / avg_time_per_lap

    # Convert the average speed to m/s
    avg_speed_mps = avg_speed / 3.6

    # Return the result
    result = round(avg_speed_mps, 2)
    return result

print(solution())