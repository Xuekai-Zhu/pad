def solution():
    """Janet starts driving across a lake in a speedboat going 30 miles per hour. Her sister follows in a sailboat that has a speed of 12 miles per hour. If the lake is 60 miles wide, how long does Janet have to wait on the other side for her sister to catch up?"""
    # Define the speed of Janet's boat and her sister's sailboat
    JANET_SPEED = 30
    SISTER_SPEED = 12

    # Define the width of the lake
    LAKE_WIDTH = 60

    # Calculate the time it takes for Janet to cross the lake
    time_janet = LAKE_WIDTH / JANET_SPEED

    # Calculate the distance Janet's sister travels during that time
    distance_sister = time_janet * SISTER_SPEED

    # Calculate the time it takes for Janet's sister to catch up
    time_sister = distance_sister / (JANET_SPEED - SISTER_SPEED)

    # Display the time Janet has to wait for her sister to catch up
    result = time_sister
    return result

print(solution())