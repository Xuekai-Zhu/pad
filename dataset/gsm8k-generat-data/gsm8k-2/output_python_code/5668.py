def solution():
    """Jett bought a cow from the market at $600 and took it to his farm. He spent $20 every day to buy food. He also used $500 to vaccinate and deworm the cow. If he sold the cow for $2500 after 40 days, calculate the profit he made from selling back the cow to the market."""
    cow_cost = 600
    food_cost = 20 * 40
    medical_cost = 500
    total_cost = cow_cost + food_cost + medical_cost
    selling_price = 2500
    profit = selling_price - total_cost
    result = profit
    return result

print(solution())