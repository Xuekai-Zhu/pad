def solution():
    buying_price = 12
    selling_price = buying_price * 1.25  # 25% profit
    num_pots = 150

    # Calculate the total revenue from selling 150 pots
    total_revenue = selling_price * num_pots

    # Calculate the profit earned by Françoise
    total_profit = total_revenue - (buying_price * num_pots)

    # Calculate the amount given back to the association
    association_share = total_profit / 2
    result = association_share
    return result

print(solution())