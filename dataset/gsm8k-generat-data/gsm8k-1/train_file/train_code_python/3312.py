def solution():
    """Marco uses a fifth of an ounce of dry tea leaves to brew his morning cup of tea each day. He buys tea leaves in boxes of 28 ounces. How many weeks of daily tea does Marco get from a box?"""
    tea_per_day = 1/5
    ounces_per_box = 28
    cups_per_box = ounces_per_box / tea_per_day
    weeks_per_box = cups_per_box / 7
    result = weeks_per_box
    return result

print(solution())