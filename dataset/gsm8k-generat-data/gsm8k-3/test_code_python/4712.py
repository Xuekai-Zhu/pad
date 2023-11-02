def solution():
    """Tony exercises every morning by walking 3 miles carrying a 25-pound backpack, then he runs another 10 miles without the backpack.  If he walks at a speed of 3 miles per hour and runs at a speed of 5 miles per hour, how many hours each week does he spend exercising?"""
    # Define the distance walked and ran each day
    DISTANCE_WALKED = 3
    DISTANCE_RUN = 10

    # Define Tony's walking and running speeds
    WALKING_SPEED = 3
    RUNNING_SPEED = 5

    # Calculate the time spent walking and running each day
    time_walked = DISTANCE_WALKED / WALKING_SPEED
    time_ran = DISTANCE_RUN / RUNNING_SPEED

    # Calculate the total time spent exercising each day
    total_time = time_walked + time_ran

    # Calculate the total time spent exercising each week
    weekly_time = total_time * 7

    # Display the total time spent exercising each week
    result = weekly_time
    return result

print(solution())