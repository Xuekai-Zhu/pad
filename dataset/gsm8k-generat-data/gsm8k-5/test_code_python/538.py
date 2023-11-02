def solution():
    bag_cost = 3000  # The luxury bag costs $3000
    profit_percent = 15  # The reseller wants a 15% profit
    profit_amount = bag_cost * (profit_percent / 100)  # Calculate the profit amount
    selling_price = bag_cost + profit_amount  # Calculate the selling price
    result = selling_price
    return result

print(solution())