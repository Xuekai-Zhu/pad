def solution():
    
    # Define the average speed of Elvis
    AVERAGE_SPEED = 18

    # Define the time Elvis travels west and east
    west_time = 5
    east_time = 8

    # Calculate the distance Elvis travels west and east
    distance_west = west_time * AVERAGE_SPEED
    distance_east = east_time * AVERAGE_SPEED

    # Calculate the total distance Elvis travels
    total_distance = distance_west + distance_east

    # Display the total distance Elvis travels
    result = total_distance
    return result

print(solution())