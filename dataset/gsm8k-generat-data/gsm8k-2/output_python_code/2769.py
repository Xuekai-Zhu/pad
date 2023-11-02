def solution():
    """Robert and Teddy are planning to buy snacks for their friends. Robert orders five boxes of pizza at $10 each box and ten cans of soft drinks at $2 each. Teddy buys six hamburgers at $3 each and an additional ten cans of soft drinks. How much do they spend in all?"""
    robert_pizza_cost = 5 * 10
    robert_drinks_cost = 10 * 2
    teddy_hamburger_cost = 6 * 3
    teddy_drinks_cost = 10 * 2
    total_cost = robert_pizza_cost + robert_drinks_cost + teddy_hamburger_cost + teddy_drinks_cost
    result = total_cost
    return result

print(solution())