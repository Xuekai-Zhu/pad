def solution():
    # Define the speed of the speedboat and the sailboat
    speedboat_speed = 30
    sailboat_speed = 12

    # Define the distance and the time it would take for each boat to cross the lake
    distance = 60
    speedboat_time = distance / speedboat_speed
    sailboat_time = distance / sailboat_speed

    # Calculate the wait time for Janet
    wait_time = sailboat_time - speedboat_time
    result = wait_time
    return result

print(solution())