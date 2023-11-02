def solution():
    """Jerry was asked by her mom to do grocery shopping. He needs to buy 2 liters of mustard oil that costs $13 per liter, 3 pounds of gluten-free penne pasta that costs $4 per pound, and 1 pound of pasta sauce that costs $5. If Jerry can keep the rest of the $50 after grocery shopping, how much money will he have?"""
    # Calculate the cost of 2 liters of mustard oil
    oil_cost = 2 * 13

    # Calculate the cost of 3 pounds of gluten-free penne pasta
    pasta_cost = 3 * 4

    # Calculate the cost of 1 pound of pasta sauce
    sauce_cost = 5

    # Calculate the total cost of the groceries
    total_cost = oil_cost + pasta_cost + sauce_cost

    # Calculate the remaining money after grocery shopping
    remaining_money = 50 - total_cost

    result = remaining_money
    return result

print(solution())