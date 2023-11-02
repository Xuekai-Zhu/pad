def solution():
    """A camping site recorded a total of 150 campers for the past three weeks. Two weeks ago, there were 40 campers which was 10 more than the number of campers three weeks ago. How many campers were there last week?"""
    # Define variables
    total_campers = 150
    campers_two_weeks_ago = 40
    campers_three_weeks_ago = campers_two_weeks_ago - 10

    # Calculate the number of campers last week
    campers_last_week = total_campers - campers_two_weeks_ago - campers_three_weeks_ago

    # Display the number of campers last week
    result = campers_last_week
    return result

print(solution())