def solution():
    
    # Define the distances
    steve_distance = 3
    tim_distance = 2

    # Define the speeds
    steve_speed = 440
    tim_speed = 264

    # Calculate the time it takes for Steve to ride his bike
    steve_time = steve_distance / steve_speed

    # Calculate the time it takes for Tim to ride his skateboard
    tim_time = tim_distance / tim_speed

    # Calculate the total time it takes for the winner to finish the race
    total_time = steve_time + tim_time

    # Display the total time
    result = total_time
    return result

print(solution())