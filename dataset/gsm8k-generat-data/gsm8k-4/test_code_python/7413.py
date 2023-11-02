def solution():
    """Company A and Company B merge. Company A receives 60% of the combined profits under the new merger, and company B receives 40% of the profits. If company B gets a total of $60000 in profit, how much does company A get?"""
    # Define the percentage of profits that company A receives
    percent_A = 0.6

    # Define the percentage of profits that company B receives
    percent_B = 1 - percent_A

    # Define the profit received by company B
    profit_B = 60000

    # Calculate the total combined profits
    total_profit = profit_B / percent_B

    # Calculate the profit received by company A
    profit_A = total_profit * percent_A

    result = profit_A
    return result

print(solution())