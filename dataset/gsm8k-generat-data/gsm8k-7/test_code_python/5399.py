def solution():
    total_copies_sold = 1000000
    advance_copies = 100000
    price_per_copy = 2.0
    agent_commission_rate = 0.1

    # Calculate the number of copies sold after deducting the advance copies
    actual_copies_sold = total_copies_sold - advance_copies

    # Calculate the total revenue earned from the actual copies sold
    total_revenue = actual_copies_sold * price_per_copy

    # Calculate the agent's commission on the revenue
    agent_commission = total_revenue * agent_commission_rate

    # Calculate the final amount earned by Steve after deducting the agent's commission
    final_earnings = total_revenue - agent_commission
    result = final_earnings
    return result

print(solution())