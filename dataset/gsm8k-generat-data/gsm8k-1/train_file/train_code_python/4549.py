def solution():
    """Johannes owns a vegetable shop, he sells cabbage for $2 per kilogram. If Johannes was able to earn $30 last Wednesday, $24 last Friday, and $42 today, how many kilograms of cabbage was he able to sell?"""
    price_per_kg = 2
    total_sales = 30 + 24 + 42
    total_kg_sold = total_sales / price_per_kg
    result = total_kg_sold
    return result

print(solution())