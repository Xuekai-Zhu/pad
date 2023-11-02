def solution():
    """A camping site recorded a total of 150 campers for the past three weeks. Two weeks ago, there were 40 campers which was 10 more than the number of campers three weeks ago. How many campers were there last week?"""
    total_campers = 150
    two_weeks_ago = 40
    three_weeks_ago = two_weeks_ago - 10
    last_week = total_campers - (two_weeks_ago + three_weeks_ago)
    result = last_week
    return result

print(solution())