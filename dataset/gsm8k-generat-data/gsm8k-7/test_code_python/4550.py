def solution():
    price_per_kg = 2
    sale1 = 30
    sale2 = 24
    sale3 = 42

    # Calculate the total amount earned from selling cabbage
    total_sale = sale1 + sale2 + sale3

    # Calculate the total weight of cabbage sold
    total_weight = total_sale / price_per_kg
    result = total_weight
    return result

print(solution())