def solution():
    """Jeremy's uncle gave him $50 to spend on basketball equipment. He bought 5 jerseys that cost $2 each, a basketball that cost $18, and a pair of shorts that cost $8. How much money does Jeremy have left?"""
    total_cost = (5 * 2) + 18 + 8
    money_left = 50 - total_cost
    result = money_left
    return result

print(solution())