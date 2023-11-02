def solution():
    """Bruce's aunt gave him $71 to spend on clothes at the mall. He bought 5 shirts that cost $5 each and a pair of pants that cost $26. How much money does Bruce have left to buy more clothes?"""
    total_spent = (5 * 5) + 26
    money_left = 71 - total_spent
    result = money_left
    return result

print(solution())