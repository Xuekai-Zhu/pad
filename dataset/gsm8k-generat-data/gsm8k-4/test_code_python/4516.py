def solution():
    """Ian used a grocery delivery app to have his groceries delivered. His original order was $25 before delivery and tip. He noticed that 3 items changed on his order. A $0.99 can of tomatoes was replaced by a $2.20 can of tomatoes, his $1.00 lettuce was replaced with $1.75 head of lettuce and his $1.96 celery was replaced with celery that cost $2.00. Delivery and tip came to a total of $8.00. How much is his new bill now, with the food substitutes and delivery/tip?"""
    # Define the original cost of the order and the cost of the substitutes
    original_cost = 25
    substitutes_cost = 2.20 + 1.75 + 2.00

    # Calculate the new cost of the order including the substitutes
    new_cost = original_cost + substitutes_cost

    # Add the cost of delivery and tip
    new_cost += 8.00

    # Return the result
    result = new_cost
    return result

print(solution())