def solution():
    # Define John's initial running time and speed
    initial_time = 8
    initial_speed = 8

    # Calculate John's increased running time and speed
    increased_time = initial_time * 1.75
    increased_speed = initial_speed + 4

    # Calculate the distance John can run using his increased time and speed
    distance = increased_time * increased_speed
    result = distance
    return result

print(solution())