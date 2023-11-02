def solution():
    # Calculate Robert's order
    robert_pizza = 5 * 10  # 5 boxes of pizza at $10 per box
    robert_drinks = 10 * 2  # 10 cans of soft drinks at $2 per can

    # Calculate Teddy's order
    teddy_hamburgers = 6 * 3  # 6 hamburgers at $3 each
    teddy_drinks = 10 * 2  # 10 cans of soft drinks at $2 per can

    # Calculate the total amount spent
    total_cost = robert_pizza + robert_drinks + teddy_hamburgers + teddy_drinks
    result = total_cost
    return result

print(solution())