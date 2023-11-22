def solution():
    
    # Define the speed of the car in the fast lane
    fast_speed = 60

    # Define the speed of the car in the slow lane
    slow_speed = fast_speed / 2

    # Define the distance traveled by the car in the fast lane
    fast_distance = 480

    # Calculate the time it takes the car to cover the same distance
    time = fast_distance / slow_speed

    # Display the time
    result = time
    return result

print(solution())