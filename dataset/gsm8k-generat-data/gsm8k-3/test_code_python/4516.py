def solution():
    """Ian used a grocery delivery app to have his groceries delivered.  His original order was $25 before delivery and tip.  He noticed that 3 items changed on his order.  A $0.99 can of tomatoes was replaced by a $2.20 can of tomatoes, his $1.00 lettuce was replaced with $1.75 head of lettuce and his $1.96 celery was replaced with celery that cost $2.00. Delivery and tip came to a total of $8.00.  How much is his new bill now, with the food substitutes and delivery/tip?"""
    # Define the original order total, delivery and tip amount
    order_total = 25
    delivery_tip = 8

    # Define the cost of each substituted item
    tomatoes_cost = 2.20
    lettuce_cost = 1.75
    celery_cost = 2.00

    # Calculate the new total cost of the order with substitutions
    new_total = order_total - 0.99 + tomatoes_cost - 1.00 + lettuce_cost - 1.96 + celery_cost + delivery_tip

    # Display the new total cost of the order
    result = new_total
    return result

print(solution())