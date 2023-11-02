def solution():
    """Sarah’s basketball games are 4 quarters that are each 12 minutes long. In the last quarter, there was a tie so the game was extended for five minutes. How long did the entire game last?"""
    quarters = 4
    minutes_per_quarter = 12
    extra_minutes = 5
    total_minutes = (quarters * minutes_per_quarter) + extra_minutes
    result = total_minutes
    return result

print(solution())