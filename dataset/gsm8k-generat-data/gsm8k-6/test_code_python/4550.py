def solution():
    # Calculate the total amount earned from selling cabbage
    total_earned = 30 + 24 + 42  # in dollars
    price_per_kg = 2  # in dollars
    total_kg_sold = total_earned / price_per_kg
    result = total_kg_sold
    return result

print(solution())