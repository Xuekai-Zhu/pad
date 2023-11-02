def solution():
    """Allen ordered five boxes of pizza, which cost $7 each box. He then gave a tip which amounts to 1/7 of the total cost of his order. If he gave the delivery man $100, how much change did he receive?"""
    box_cost = 7
    total_cost = box_cost * 5
    tip = total_cost / 7
    total_cost_with_tip = total_cost + tip
    payment = 100
    change = payment - total_cost_with_tip
    result = change
    return result

print(solution())