def solution():
    silver_weight = 1.5
    gold_weight = 3.0  # 1.5 ounces of silver is twice as much as 3 ounces of gold
    silver_price_per_oz = 20
    gold_price_per_oz = silver_price_per_oz * 50  # gold is 50 times more expensive than silver

    # Calculate the cost of the silver
    silver_cost = silver_weight * silver_price_per_oz

    # Calculate the cost of the gold
    gold_cost = gold_weight * gold_price_per_oz

    # Calculate the total cost of everything
    total_cost = silver_cost + gold_cost
    result = total_cost
    return result

print(solution())