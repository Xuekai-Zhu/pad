def solution():
    """Janet Starts driving across a lake in a speedboat going 30 miles per hour. Her sister follows in a sailboat that has a speed of 12 miles per hour. If the lake is 60 miles wide, how long does Janet have to wait on the other side for her sister to catch up?"""
    # Define the speeds of the speedboat and the sailboat
    speedboat_speed = 30
    sailboat_speed = 12

    # Define the distance to be covered
    distance = 60

    # Calculate the time it would take Janet to cross the lake
    time_janet = distance / speedboat_speed

    # Calculate the distance Janet's sister covers in that time
    distance_sister = sailboat_speed * time_janet

    # Calculate the time Janet has to wait for her sister to catch up
    time_wait = time_janet - (distance_sister / speedboat_speed)

    # Return the result
    result = time_wait
    return result

print(solution())