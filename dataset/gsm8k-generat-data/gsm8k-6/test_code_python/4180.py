def solution():
    # Calculate the cost of one year's worth of soap
    cost_per_month = 8  # cost of one bar of soap that lasts for 2 months
    months_per_year = 12  
    bars_per_year = months_per_year / 2  # she needs one bar of soap every 2 months
    total_cost = cost_per_month * bars_per_year
    result = total_cost
    return result

print(solution())