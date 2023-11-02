def solution():
    # Define John's speed in m/s
    john_speed = 100 / 13

    # Calculate John's acceleration in m/s^2
    john_acceleration = (john_speed - 4) / 12

    # Define James's speed in m/s
    james_speed = john_speed + 2

    # Calculate James's acceleration in m/s^2
    james_acceleration = (james_speed - 5) / 8

    # Calculate the time for James to run the last 90 meters
    james_time_last_90 = ((90 / james_speed) / 2) * 2

    # Calculate the time for James to run the first 10 meters
    james_time_first_10 = 2

    # Calculate the time for James to reach his top speed
    james_time_top_speed = (james_speed - 5) / james_acceleration

    # Calculate James's total time to run 100 meters
    james_total_time = james_time_top_speed + james_time_first_10 + james_time_last_90

    result = james_total_time
    return result

print(solution())