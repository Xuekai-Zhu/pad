def solution():
    # Calculate Micah's speed relative to Dean's
    micah_speed = 2/3
    dean_speed = 1
    jake_speed = micah_speed * (4/3)

    # Calculate the time it takes each person to finish the marathon
    micah_time = 26.2 / micah_speed
    dean_time = 26.2 / dean_speed
    jake_time = 26.2 / jake_speed

    # Calculate the total time for all three to finish
    total_time = micah_time + dean_time + jake_time
    result = total_time
    return result

print(solution())