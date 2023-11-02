def solution():
    """On a road map, 1/4 inch represents 8 miles of actual road distance. The towns of Pence and Hillcrest are represented by points 3 3/8 inches apart on the map. What is the actual distance, in miles, between the towns?"""
    # Define the scale of the map
    SCALE = 8 / (1/4)

    # Define the distance represented by the distance between the towns on the map
    map_distance = 3 + 3/8

    # Calculate the actual distance between the towns
    actual_distance = map_distance * SCALE

    # Display the actual distance
    result = actual_distance
    return result

print(solution())