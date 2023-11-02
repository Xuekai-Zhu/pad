def solution():
    """Rhonda, Sally, and Diane are members of their school's track team.  The three of them run the 600-meter relay race together. Rhonda runs the first 200 meters of the race, Sally runs the second 200 meters of the race, and Diane runs the final 200 meters of the race. Rhonda can run 200 meters in 24 seconds.  Sally takes two seconds longer to run the same distance, while Diane can run 200 meters three seconds faster than Rhonda.  How many seconds does it take for the three of them to run the 600-meter relay race?"""
    # Define the distance each runner covers and their respective speeds
    R_DISTANCE = 200
    R_SPEED = 24
    S_DISTANCE = 200
    S_SPEED = 26
    D_DISTANCE = 200
    D_SPEED = 21

    # Calculate the time each runner takes to cover their respective distances
    r_time = R_SPEED
    s_time = S_SPEED
    d_time = D_SPEED - 3

    # Calculate the total time taken for the relay race
    total_time = r_time + s_time + d_time

    result = total_time
    return result

print(solution())