def solution():
    """Frank and Bill have $42 and they bought 3 large pizzas with the money. Each pizza cost $11 and Frank paid for all three pizzas. Frank gave the rest of his money to Bill. If Bill had $30 already, how much money does Bill have now?"""
    # Define the cost of each pizza
    PIZZA_COST = 11

    # Calculate the total cost of the pizzas
    total_cost = PIZZA_COST * 3

    # Calculate Frank's money remaining after buying the pizzas
    frank_money = 42 - total_cost

    # Calculate Bill's total money (including his initial $30)
    bill_money = frank_money + 30

    # Return the result
    result = bill_money
    return result

print(solution())