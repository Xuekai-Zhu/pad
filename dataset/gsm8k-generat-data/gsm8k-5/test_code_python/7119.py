def solution():
    oil_cost = 13 * 2  # Jerry needs to buy 2 liters of mustard oil that costs $13 per liter
    pasta_cost = 4 * 3  # Jerry needs to buy 3 pounds of gluten-free penne pasta that costs $4 per pound
    sauce_cost = 5  # Jerry needs to buy 1 pound of pasta sauce that costs $5
    total_cost = oil_cost + pasta_cost + sauce_cost  # Calculate the total cost of groceries
    remaining_money = 50 - total_cost  # Calculate the remaining money after grocery shopping
    result = remaining_money
    return result

print(solution())