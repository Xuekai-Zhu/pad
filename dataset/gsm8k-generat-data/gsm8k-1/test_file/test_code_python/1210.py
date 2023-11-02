def solution():
    """Jordan has 2 children who wear diapers. Each child requires 5 diaper changes per day. Jordan's wife changes half of the diapers. How many diapers does Jordan change per day?"""
    children = 2
    daily_changes = 5
    wife_changes = children * daily_changes / 2
    jordan_changes = children * daily_changes - wife_changes
    result = jordan_changes
    return result

print(solution())