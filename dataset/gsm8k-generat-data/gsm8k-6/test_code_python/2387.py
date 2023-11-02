def solution():
    # Calculate the total revenue from selling amulets
    revenue = 2 * 25 * (40-30) * 40  # 2 days selling, 25 amulets sold each day, $40 selling price, $30 cost to make
    faire_cut = 0.1 * revenue  # calculate faire's cut
    profit = revenue - faire_cut  # calculate profit
    result = profit
    return result

print(solution())