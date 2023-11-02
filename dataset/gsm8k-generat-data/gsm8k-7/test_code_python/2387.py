def solution():
    num_days = 2
    num_amulets_per_day = 25
    selling_price = 40
    cost_price = 30
    faire_cut = 0.1

    # Calculate the total number of amulets sold
    total_amulets_sold = num_days * num_amulets_per_day

    # Calculate the total revenue from selling all amulets
    total_revenue = total_amulets_sold * selling_price

    # Calculate the total cost of making all amulets
    total_cost = total_amulets_sold * cost_price

    # Calculate the faire's cut of the revenue
    faire_rev_cut = total_revenue * faire_cut

    # Calculate the profit after paying for the cost and faire's cut
    profit = total_revenue - total_cost - faire_rev_cut
    result = profit
    return result

print(solution())