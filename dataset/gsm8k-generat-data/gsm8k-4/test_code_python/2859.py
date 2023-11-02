def solution():
    """Allen ordered five boxes of pizza, which cost $7 each box. He then gave a tip which amounts to 1/7 of the total cost of his order. If he gave the delivery man $100, how much change did he receive?"""
    # Calculate the total cost of the pizza boxes
    pizza_cost = 7 * 5

    # Calculate the amount of tip
    tip = pizza_cost / 7

    # Calculate the total amount paid by Allen
    total_amount = pizza_cost + tip

    # Calculate the change received by Allen
    change = 100 - total_amount

    # return the result
    result = change
    return result

print(solution())