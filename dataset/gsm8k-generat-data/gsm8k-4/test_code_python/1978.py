def solution():
    """Every Monday to Friday morning, Alice walks 10 miles through a large grass field to get to school. To avoid the hot afternoon sun on her way home, she walks 12 miles through a forest. When she gets home on Friday, how many miles will she have walked that week?"""
    # Calculate the distance that Alice walks every day
    daily_distance = 10 + 12

    # Calculate the distance that Alice walks from Monday to Friday
    weekly_distance = daily_distance * 5

    # Return the result
    result = weekly_distance
    return result

print(solution())