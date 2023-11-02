def solution():
    """Bob has planted corn in his garden, and it has just started to sprout. A week after planting it, it had grown 2 inches. The next week, its height increased by twice as much as it had the first week. In the third week, it grew 4 times as much as it did the week before. How tall are the corn plants now?"""
    week_1_growth = 2
    week_2_growth = 2 * week_1_growth
    week_3_growth = 4 * week_2_growth
    total_growth = week_1_growth + week_2_growth + week_3_growth
    result = total_growth
    return result

print(solution())