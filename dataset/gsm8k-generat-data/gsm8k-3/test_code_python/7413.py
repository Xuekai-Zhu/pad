def solution():
    """Company A and Company B merge. Company A receives 60% of the combined profits under the new merger, and company B receives 40% of the profits. If company B gets a total of $60000 in profit, how much does company A get?"""
    # Define the percentage of profits received by Company A and Company B
    A_PERCENT = 0.6
    B_PERCENT = 0.4

    # Define the total profit made by both companies
    total_profit = 60000 / B_PERCENT

    # Calculate the profit received by Company A
    A_profit = total_profit * A_PERCENT

    # Display the profit received by Company A
    result = A_profit
    return result

print(solution())