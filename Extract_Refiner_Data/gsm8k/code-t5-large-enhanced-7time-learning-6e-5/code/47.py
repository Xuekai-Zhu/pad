def solution():
    
    # Define the initial speed and the time taken to travel back
    initial_speed = 10
    time_back = 0

    # Calculate the distance traveled
    distance = initial_speed * (4/60)

    # Calculate the time taken to travel back
    time_back += distance / 6

    # Display the time taken to travel back
    result = time_back
    return result

print(solution())