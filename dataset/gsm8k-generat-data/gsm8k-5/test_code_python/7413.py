def solution():
    company_B_profit = 60000  # Company B gets $60000 in profit
    company_B_percentage = 0.4  # Company B receives 40% of the profits

    # Calculate the total profits
    total_profit = company_B_profit / company_B_percentage

    # Calculate the profit for company A
    company_A_profit = total_profit * 0.6  # Company A receives 60% of the profits

    result = company_A_profit
    return result

print(solution())