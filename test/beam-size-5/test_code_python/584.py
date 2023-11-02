def solution():
    initial_speed = 47  # Jared starts with 47 words per minute
    increased_speed = 52  # Jared increased his typing speed to 52 WPM
    increased_speed_increase = 5  # Jared increases his typing speed once more by 5 words

    # Calculate the new typing speed after increasing by 5 words
    new_speed = initial_speed + (increase * increased_speed_increase)

    # Calculate the average of the three measurements
    average_speed = (new_speed - increased_speed) / 3
    result = average_speed
    return result

print(solution())