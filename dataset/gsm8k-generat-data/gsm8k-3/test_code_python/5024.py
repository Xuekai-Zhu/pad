def solution():
    """John trains for ultramarathons.  He starts only able to run 8 hours straight but eventually increases that by 75%.  He also increases his speed of 8 mph by 4 mph.  How far can he run now?"""
    # Define John's initial running time and speed
    initial_time = 8
    initial_speed = 8

    # Calculate John's increased running time and speed
    increased_time = initial_time * 1.75
    increased_speed = initial_speed + 4

    # Calculate the distance John can run at his increased time and speed
    distance = increased_time * increased_speed

    # Display the distance John can run
    result = distance
    return result

print(solution())