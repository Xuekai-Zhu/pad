def solution():
    company_b_profit = 60000
    company_b_percentage = 0.4

    # Calculate the total combined profits
    total_profit = company_b_profit / company_b_percentage

    # Calculate the profit percentage of company A
    company_a_percentage = 0.6

    # Calculate the profit of company A
    company_a_profit = total_profit * company_a_percentage
    result = company_a_profit
    return result

print(solution())