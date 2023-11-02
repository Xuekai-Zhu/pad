def solution():
    """Every Monday to Friday morning, Alice walks 10 miles through a large grass field to get to school. To avoid the hot afternoon sun on her way home, she walks 12 miles through a forest. When she gets home on Friday, how many miles will she have walked that week?"""
    grass_field_distance = 10
    forest_distance = 12
    total_distance_per_day = grass_field_distance + forest_distance
    total_distance_per_week = total_distance_per_day * 5
    result = total_distance_per_week
    return result

print(solution())