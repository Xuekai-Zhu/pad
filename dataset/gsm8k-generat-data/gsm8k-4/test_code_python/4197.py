def solution():
    """Chantal knits sweaters to sell. Each sweater takes 4 balls of yarn. Each ball of yarn costs $6. How much money will Chantal gain in all 28 sweaters if she sells each sweater for $35?"""
    # Define the cost for each ball of yarn and the number of balls needed for each sweater
    BALL_OF_YARN_COST = 6
    BALLS_PER_SWEATER = 4

    # Define the selling price for each sweater
    SWEATER_SELLING_PRICE = 35

    # Calculate the total cost for all the yarn needed
    total_yarn_cost = BALL_OF_YARN_COST * BALLS_PER_SWEATER * 28

    # Calculate the total revenue from selling all the sweaters
    total_revenue = SWEATER_SELLING_PRICE * 28

    # Calculate the total profit
    total_profit = total_revenue - total_yarn_cost

    # return the result
    result = total_profit
    return result

print(solution())