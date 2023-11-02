def solution():
    """Company A and Company B merge. Company A receives 60% of the combined profits under the new merger, and company B receives 40% of the profits. If company B gets a total of $60000 in profit, how much does company A get?"""
    company_b_profit = 60000
    company_b_percent = 40
    company_a_percent = 60
    total_combined_profit = company_b_profit / (company_b_percent / 100)
    company_a_profit = total_combined_profit * (company_a_percent / 100)
    result = company_a_profit
    return result

print(solution())