def solution():
    """Marco uses a fifth of an ounce of dry tea leaves to brew his morning cup of tea each day. He buys tea leaves in boxes of 28 ounces. How many weeks of daily tea does Marco get from a box?"""
    daily_usage = 1/5
    box_size = 28
    weeks_of_tea = box_size / (daily_usage * 7)
    result = weeks_of_tea
    return result

print(solution())