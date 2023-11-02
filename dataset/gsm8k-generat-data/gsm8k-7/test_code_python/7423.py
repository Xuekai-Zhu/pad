def solution():
    rice_weight = 50  # in kilograms
    cost_price = 50
    selling_price_per_kg = 1.20

    # Calculate the total selling price for the entire sack of rice
    selling_price = rice_weight * selling_price_per_kg

    # Calculate the profit
    profit = selling_price - cost_price

    result = profit
    return result

print(solution())