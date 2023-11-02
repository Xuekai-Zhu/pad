def solution():
    """On a road map, 1/4 inch represents 8 miles of actual road distance. The towns of Pence and Hillcrest are represented by points 3 3/8 inches apart on the map. What is the actual distance, in miles, between the towns?"""
    map_scale = 1/4 # inch
    actual_scale = 8 # miles
    distance_on_map = 3 + 3/8 # inches
    distance_in_miles = distance_on_map * map_scale * actual_scale
    result = distance_in_miles
    return result

print(solution())