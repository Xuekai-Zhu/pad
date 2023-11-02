def solution():
    original_price = 80000  # Mrs. Choi purchased the house for $80000
    profit_percent = 20  # She sold the house for a 20% profit
    commission_percent = 5  # She paid a 5% broker's commission on the original price

    # Calculate the profit made on the original price
    profit = original_price * (profit_percent / 100)

    # Calculate the selling price of the house
    selling_price = original_price + profit

    # Calculate the broker's commission on the original price
    commission = original_price * (commission_percent / 100)

    # Calculate the final selling price of the house after paying the broker's commission
    final_selling_price = selling_price - commission
    result = final_selling_price
    return result

print(solution())