def solution():
    """Jerry was asked by her mom to do grocery shopping. He needs to buy 2 liters of mustard oil that costs $13 per liter, 3 pounds of gluten-free penne pasta that costs $4 per pound, and 1 pound of pasta sauce that costs $5. If Jerry can keep the rest of the $50 after grocery shopping, how much money will he have?"""
    oil_cost = 13 * 2
    pasta_cost = 4 * 3
    sauce_cost = 5
    total_cost = oil_cost + pasta_cost + sauce_cost
    remaining_money = 50 - total_cost
    result = remaining_money
    return result

print(solution())