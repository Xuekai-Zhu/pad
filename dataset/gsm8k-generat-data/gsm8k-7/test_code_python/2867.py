def solution():
    dean_time = 9.0
    micah_speed_ratio = 2.0/3.0
    jake_time_increase_ratio = 1.0/3.0

    # Calculate Micah's speed and time
    micah_speed = micah_speed_ratio * (1.0/dean_time)
    micah_time = 1.0/micah_speed

    # Calculate Jake's time
    jake_time = micah_time * (1.0 + jake_time_increase_ratio)

    # Calculate the total time
    total_time = dean_time + micah_time + jake_time
    result = total_time
    return result

print(solution())