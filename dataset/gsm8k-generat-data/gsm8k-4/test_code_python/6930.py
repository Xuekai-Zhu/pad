def solution():
    """Josh has 9 dollars. He spent $1.75 on a drink, and then spent another $1.25. How much money, in dollars, does Josh have left?"""
    # Define the initial amount of money Josh has
    amount = 9

    # Subtract the cost of the first purchase
    amount -= 1.75

    # Subtract the cost of the second purchase
    amount -= 1.25

    # return the result
    result = amount
    return result

print(solution())