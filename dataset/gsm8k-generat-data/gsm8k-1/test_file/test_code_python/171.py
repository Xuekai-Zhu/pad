def solution():
    """Juan and his brother Carlos are selling lemonade. For each gallon they make it costs $3 for lemons and $2 for sugar. They sell each glass for $0.50 and get 20 glasses per gallon. If they made $25 in profit, how much did they spend on lemons?"""
    cost_per_gallon = 3 + 2
    revenue_per_gallon = 20 * 0.5
    profit_per_gallon = revenue_per_gallon - cost_per_gallon
    total_profit = 25
    gallons_sold = total_profit / profit_per_gallon
    cost_of_lemons = gallons_sold * 3
    result = cost_of_lemons
    return result

print(solution())