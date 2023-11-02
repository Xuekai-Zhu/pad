def solution():
    """A camping site recorded a total of 150 campers for the past three weeks. Two weeks ago, there were 40 campers which was 10 more than the number of campers three weeks ago. How many campers were there last week?"""
    # Define the total number of campers
    total_campers = 150

    # Calculate the number of campers three weeks ago
    campers_three_weeks_ago = (total_campers - 40) - 10

    # Calculate the number of campers last week
    campers_last_week = total_campers - campers_three_weeks_ago - 40

    # return the result
    result = campers_last_week
    return result

print(solution())