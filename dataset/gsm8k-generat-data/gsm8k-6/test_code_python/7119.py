def solution():
    # Calculate the total cost of the grocery shopping
    mustard_oil_cost = 2 * 13  # 2 liters of mustard oil that costs $13 per liter
    penne_pasta_cost = 3 * 4  # 3 pounds of gluten-free penne pasta that costs $4 per pound
    pasta_sauce_cost = 5  # 1 pound of pasta sauce that costs $5
    total_cost = mustard_oil_cost + penne_pasta_cost + pasta_sauce_cost

    # Calculate the remaining amount of money for Jerry
    remaining_money = 50 - total_cost
    result = remaining_money
    return result

print(solution())