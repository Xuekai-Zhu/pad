def solution():
    """Ian used a grocery delivery app to have his groceries delivered. His original order was $25 before delivery and tip. He noticed that 3 items changed on his order. A $0.99 can of tomatoes was replaced by a $2.20 can of tomatoes, his $1.00 lettuce was replaced with $1.75 head of lettuce and his $1.96 celery was replaced with celery that cost $2.00. Delivery and tip came to a total of $8.00. How much is his new bill now, with the food substitutes and delivery/tip?"""
    original_order = 25
    new_order = original_order + 2.20 + 1.75 + 2.00
    delivery_tip = 8.00
    total_cost = new_order + delivery_tip
    result = total_cost
    return result

print(solution())