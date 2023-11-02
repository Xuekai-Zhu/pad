def solution():
    # Calculate Jenna's total revenue
    revenue = 8 * 5000

    # Calculate Jenna's total cost
    cost = 3 * 5000 + 10000 + 4 * 2500

    # Calculate Jenna's total profit
    profit = revenue - cost

    # Calculate Jenna's total taxes
    taxes = 0.2 * profit

    # Calculate Jenna's final profit or loss
    final_profit = profit - taxes

    result = final_profit
    return result

print(solution())