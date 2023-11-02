def solution():
    """Adam has an orchard. Every day for 30 days he picks 4 apples from his orchard. After a month, Adam has collected all the remaining apples, which were 230. How many apples in total has Adam collected from his orchard?"""
    daily_picks = 4
    days = 30
    remaining_apples = 230
    total_picked = (daily_picks * days) + remaining_apples
    result = total_picked
    return result

print(solution())