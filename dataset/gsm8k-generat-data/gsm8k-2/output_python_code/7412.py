def solution():
    """Company A and Company B merge. Company A receives 60% of the combined profits under the new merger, and company B receives 40% of the profits. If company B gets a total of $60000 in profit, how much does company A get?"""
    b_profit = 60000
    b_percent = 0.4
    a_percent = 0.6
    total_profit = b_profit / b_percent
    a_profit = total_profit * a_percent
    result = a_profit
    return result

print(solution())