def solution():
    """Chantal knits sweaters to sell. Each sweater takes 4 balls of yarn. Each ball of yarn costs $6. How much money will Chantal gain in all 28 sweaters if she sells each sweater for $35?"""
    # Define the cost of each ball of yarn
    YARN_COST = 6

    # Define the number of balls of yarn needed per sweater
    BALLS_PER_SWEATER = 4

    # Define the selling price per sweater
    SELLING_PRICE = 35

    # Define the number of sweaters
    NUM_SWEATERS = 28

    # Calculate the total cost of yarn
    total_yarn_cost = YARN_COST * BALLS_PER_SWEATER * NUM_SWEATERS

    # Calculate the total revenue from selling the sweaters
    total_revenue = SELLING_PRICE * NUM_SWEATERS

    # Calculate the profit
    profit = total_revenue - total_yarn_cost

    # Display the profit
    result = profit
    return result

print(solution())