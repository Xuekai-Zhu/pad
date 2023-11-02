def solution():
    """Susan had a sum of money. She spent 1/5 of it in September, 1/4 of it in October, and $120 in November. After spending these amounts of money, she still had $540 left. How much money did she have at first?"""
    # Let x be the amount of money Susan had at first
    # Susan spent 1/5 of it in September
    x -= x/5
    # Susan spent 1/4 of it in October
    x -= x/4
    # Susan spent $120 in November
    x -= 120
    # Susan still had $540 left
    x += 540
    # The final value of x is the amount of money Susan had at first
    result = x
    return result

print(solution())