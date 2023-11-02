def solution():
    initial_time = 8  # John can run for 8 hours straight initially
    increased_time = initial_time * 1.75  # John increases his running time by 75%
    initial_speed = 8  # John can run at 8 mph initially
    increased_speed = initial_speed + 4  # John increases his running speed by 4 mph

    # Calculate the distance John can run now
    distance = increased_time * increased_speed
    result = distance
    return result

print(solution())