def solution():
    
    # Define the distance and speed
    distance = 150
    speed = 75

    # Calculate the time spent driving
    time = distance / speed

    # Calculate the total time spent at the museum
    total_time = time + 6

    # Calculate the distance Jack gone from home
    distance_lost = distance - time

    # Display the distance Jack gone from home
    result = distance_lost
    return result

print(solution())