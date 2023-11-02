def solution():
    """Matthew drinks 4 glasses of water per day. Each glass is 5 ounces. He decides to just buy a 35 ounces water bottle. How many times will he fill it each week?"""
    glasses_per_day = 4
    ounces_per_glass = 5
    ounces_per_bottle = 35
    bottles_per_day = ounces_per_bottle / (glasses_per_day * ounces_per_glass)
    bottles_per_week = bottles_per_day * 7
    result = bottles_per_week
    return result

print(solution())