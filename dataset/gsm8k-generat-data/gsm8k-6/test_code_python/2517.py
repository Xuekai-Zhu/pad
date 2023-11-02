def solution():
    # Calculate the selling price of the house
    original_price = 80000
    profit = 0.2 * original_price
    selling_price = original_price + profit
    commission = 0.05 * original_price
    final_price = selling_price - commission
    result = final_price
    return result

print(solution())