def solution():
    # Define the original price and the commission rate
    original_price = 80000
    commission_rate = 0.05

    # Calculate the selling price after the 20% profit
    profit = original_price * 0.2
    selling_price = original_price + profit

    # Calculate the commission amount
    commission = original_price * commission_rate

    # Calculate the final amount Mrs. Choi received after the commission
    final_amount = selling_price - commission
    result = final_amount
    return result

print(solution())