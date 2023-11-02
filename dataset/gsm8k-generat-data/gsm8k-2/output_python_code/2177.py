def solution():
    """Ben bought a lawnmower for his garden. He paid $100 for it. After six months, the value of the mower dropped by about 25%. Over the next year, the value of the mower dropped another 20% in value. How much is Ben's lawnmower worth after this time?"""
    initial_value = 100
    six_month_value = initial_value * 0.75
    final_value = six_month_value * 0.8
    result = final_value
    return result

print(solution())