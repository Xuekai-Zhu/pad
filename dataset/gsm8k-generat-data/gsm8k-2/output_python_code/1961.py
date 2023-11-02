def solution():
    """Philip is a painter. He makes 2 paintings per day. If he already has 20 paintings, how many paintings in total will he have after 30 days?"""
    starting_paintings = 20
    paintings_per_day = 2
    days = 30
    total_paintings = starting_paintings + (paintings_per_day * days)
    result = total_paintings
    return result

print(solution())