def solution():
    """
    Bob has planted corn in his garden, and it has just started to sprout. 
    A week after planting it, it had grown 2 inches. The next week, 
    its height increased by twice as much as it had the first week. 
    In the third week, it grew 4 times as much as it did the week before. 
    How tall are the corn plants now?
    """
    week_one = 2
    week_two = week_one * 2
    week_three = week_two * 4
    total_height = week_one + week_two + week_three
    result = total_height
    return result

print(solution())