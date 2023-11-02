def solution():
    """Dan can get to the center of a lollipop in 58 licks.  Micheal does it in 63 licks. Sam & David each take 70 licks to get to the center of a lollipop while Lance only needs 39 licks. What is the average amount of licks it takes to get to the center of a lollipop?"""
    dan_licks = 58
    michael_licks = 63
    sam_licks = 70
    david_licks = 70
    lance_licks = 39
    total_licks = dan_licks + michael_licks + sam_licks + david_licks + lance_licks
    num_people = 5
    avg_licks = total_licks / num_people
    result = avg_licks
    return result

print(solution())