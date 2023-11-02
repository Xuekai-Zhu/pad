def solution():
    """A camping site recorded a total of 150 campers for the past three weeks. Two weeks ago, there were 40 campers which was 10 more than the number of campers three weeks ago. How many campers were there last week?"""
    total_campers = 150
    campers_2_weeks_ago = 40
    campers_3_weeks_ago = campers_2_weeks_ago - 10
    campers_last_week = total_campers - campers_2_weeks_ago - campers_3_weeks_ago
    result = campers_last_week
    return result

print(solution())