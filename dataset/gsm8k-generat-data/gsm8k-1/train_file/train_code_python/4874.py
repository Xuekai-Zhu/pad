def solution():
    """Tony drinks 72 ounces of water per day. He decides that to stop wasting plastic, he will buy a reusable metal bottle. If he buys an 84-ounce water bottle, how many times will he fill it each week?"""
    ounces_per_day = 72
    ounces_per_bottle = 84
    fill_per_week = int((ounces_per_day * 7) / ounces_per_bottle)
    result = fill_per_week
    return result

print(solution())