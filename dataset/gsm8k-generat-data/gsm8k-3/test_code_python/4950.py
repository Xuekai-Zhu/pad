def solution():
    """It takes Jerome 6 hours to run the trail around the park and it takes Nero 3 hours. If Jerome runs at 4 MPH, what speed (in MPH) does Nero run in the park?"""
    # Define the time and speed of Jerome
    j_time = 6
    j_speed = 4

    # Define the time of Nero
    n_time = 3

    # Calculate the distance around the park
    distance = j_time * j_speed

    # Calculate the speed of Nero
    n_speed = distance / n_time

    # Display Nero's speed
    result = n_speed
    return result

print(solution())