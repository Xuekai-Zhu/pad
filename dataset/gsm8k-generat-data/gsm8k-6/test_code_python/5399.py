def solution():
    # Calculate the total revenue from selling 1,000,000 copies
    revenue = 2 * 1000000  # Steve gets $2 for each copy sold

    # Calculate the agent's commission
    agent_commission = 0.1 * revenue  

    # Calculate the amount of money Steve kept
    money_kept = revenue - agent_commission - 100000  # Steve pays for the 100,000 advance

    result = money_kept
    return result

print(solution())