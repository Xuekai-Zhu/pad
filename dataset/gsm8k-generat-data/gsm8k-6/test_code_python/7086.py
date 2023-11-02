def solution():
    # Calculate the total earnings of the booth for 5 days
    popcorn_earnings = 50 * 5  # $50 earned each day for selling popcorn
    cotton_candy_earnings = 3 * 50 * 5  # 3 times as much earned for selling cotton candy
    total_earnings = popcorn_earnings + cotton_candy_earnings

    # Calculate the total expenses for 5 days
    total_expenses = 30 + 75  # $30 for rent and $75 for ingredients

    # Calculate the net profit for 5 days
    net_profit = total_earnings - total_expenses
    result = net_profit
    return result

print(solution())