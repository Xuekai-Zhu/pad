def solution():
    original_price = 80000
    profit_percentage = 0.2  # 20% profit
    broker_commission = 0.05  # 5% broker's commission

    # Calculate the selling price after the 20% profit
    selling_price = original_price * (1 + profit_percentage)

    # Calculate the commission Mr. Choi will pay to the broker
    commission = original_price * broker_commission

    # Calculate the final amount Mrs. Choi will receive after the commission
    final_amount = selling_price - commission
    result = final_amount
    return result

print(solution())