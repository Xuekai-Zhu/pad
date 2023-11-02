def solution():
    # Calculate the total revenue from book sales
    total_sales_revenue = 2 * 1000000

    # Calculate the revenue after the agent's commission
    agent_commission = total_sales_revenue * 0.1
    revenue_after_commission = total_sales_revenue - agent_commission

    # Calculate the revenue after subtracting the advance
    revenue_after_advance = revenue_after_commission - 100000

    result = revenue_after_advance
    return result

print(solution())