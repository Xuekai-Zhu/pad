def solution():
    """Antoine's french onion soup recipe calls for 2 pounds of onions. He likes to double that amount. His soup serves 6 people. The onions are currently on sale for $2.00 a pound. He also needs 2 boxes of beef stock, that are also on sale for $2.00 a box. What is the cost per serving? (Round to the nearest integer.)"""
    onion_cost = 2 * 2
    beef_stock_cost = 2 * 2
    total_cost = onion_cost + beef_stock_cost
    servings = 6
    cost_per_serving = total_cost / servings
    result = round(cost_per_serving)
    
    return result

print(solution())