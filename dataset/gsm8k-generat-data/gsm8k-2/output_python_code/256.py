def solution():
    """On a road map, 1/4 inch represents 8 miles of actual road distance. The towns of Pence and Hillcrest are represented by points 3 3/8 inches apart on the map. What is the actual distance, in miles, between the towns?"""
    inch_per_mile = 1 / 0.25  # 4 inches represent 32 miles
    distance_on_map = 3 + (3/8)  # inches
    actual_distance = distance_on_map * inch_per_mile
    result = actual_distance
    return result

print(solution())