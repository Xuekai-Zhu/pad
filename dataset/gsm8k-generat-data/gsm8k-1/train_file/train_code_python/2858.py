def solution():
    """Allen ordered five boxes of pizza, which cost $7 each box. He then gave a tip which amounts to 1/7 of the total cost of his order. If he gave the delivery man $100, how much change did he receive?"""
    pizza_boxes = 5
    box_cost = 7
    total_cost = pizza_boxes * box_cost
    tip_percent = 1/7
    tip_amount = tip_percent * total_cost
    total_amount = total_cost + tip_amount
    payment = 100
    change = payment - total_amount
    result = change
    return result

print(solution())