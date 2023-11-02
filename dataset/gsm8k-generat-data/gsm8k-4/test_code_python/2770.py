def solution():
    """Robert and Teddy are planning to buy snacks for their friends.  Robert orders five boxes of pizza at $10 each box and ten cans of soft drinks at $2 each. Teddy buys six hamburgers at $3 each and an additional ten cans of soft drinks. How much do they spend in all?"""
    # Calculate Robert's total cost
    robert_total = 5 * 10 + 10 * 2

    # Calculate Teddy's total cost
    teddy_total = 6 * 3 + 10 * 2

    # Calculate the total cost of both orders
    total_cost = robert_total + teddy_total

    # return the result
    result = total_cost
    return result

print(solution())