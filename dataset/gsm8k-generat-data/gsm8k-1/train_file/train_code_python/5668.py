def solution():
    """Jett bought a cow from the market at $600 and took it to his farm. He spent $20 every day to buy food. He also used $500 to vaccinate and deworm the cow. If he sold the cow for $2500 after 40 days, calculate the profit he made from selling back the cow to the market."""
    buying_price = 600
    food_cost = 20 * 40
    healthcare_cost = 500
    selling_price = 2500
    total_cost = buying_price + food_cost + healthcare_cost
    profit = selling_price - total_cost
    result = profit
    return result

print(solution())