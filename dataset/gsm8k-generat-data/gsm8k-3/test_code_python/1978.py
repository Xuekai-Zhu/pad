def solution():
    """Every Monday to Friday morning, Alice walks 10 miles through a large grass field to get to school. To avoid the hot afternoon sun on her way home, she walks 12 miles through a forest. When she gets home on Friday, how many miles will she have walked that week?"""
    # Define the distance Alice walks each way
    GRASS_FIELD_DISTANCE = 10
    FOREST_DISTANCE = 12

    # Calculate the total distance Alice walks each day
    total_distance = GRASS_FIELD_DISTANCE + FOREST_DISTANCE

    # Calculate the total distance Alice walks in a week
    weekly_distance = total_distance * 5

    # Display the total distance Alice walks in a week
    result = weekly_distance
    return result

print(solution())