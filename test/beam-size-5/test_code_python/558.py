def solution():
    
    # Define the initial angle of the pyramids
    initial_angle = 32

    # Define the speed of the sun
    sun_speed = 5

    # Define the time it takes for the sun to move to the pyramid
    time = 10

    # Calculate the distance between the sun and the pyramid
    distance = sun_speed * time

    # Calculate the final angle of the pyramids
    final_angle = initial_angle + distance

    # Display the final angle
    result = final_angle
    return result

print(solution())