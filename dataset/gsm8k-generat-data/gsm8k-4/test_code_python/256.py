def solution():
    """On a road map, 1/4 inch represents 8 miles of actual road distance. The towns of Pence and Hillcrest are represented by points 3 3/8 inches apart on the map. What is the actual distance, in miles, between the towns?"""
    # Define the scale of the map
    map_scale = 0.25

    # Calculate the actual distance represented by 1 inch on the map
    actual_distance_per_inch = 8 / map_scale

    # Calculate the actual distance between the towns
    map_distance = 3 + 3/8
    actual_distance = map_distance * actual_distance_per_inch

    # Round the result to the nearest integer
    result = round(actual_distance)
    return result

print(solution())