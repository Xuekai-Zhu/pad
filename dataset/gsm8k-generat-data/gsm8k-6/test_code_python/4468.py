def solution():
    # Calculate the total cost and revenue of face masks
    cost = 12 * 9 * 50  # cost of buying 12 boxes of face masks
    revenue_repacked = 6 * (5/25) * 50  # revenue from selling 6 repacked boxes at $5 per 25 pieces
    revenue_baggies = 300 * (3/10)  # revenue from selling 300 face masks in baggies at the rate of 10 pieces for $3
    total_revenue = revenue_repacked + revenue_baggies  # total revenue
    profit = total_revenue - cost  # profit
    result = profit
    return result

print(solution())