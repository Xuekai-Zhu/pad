def solution():
    """Andy bakes and sells birthday cakes. To make two cakes he spends $12 on ingredients, and $1 on packaging for each cake. Andy sells each cake for $15. How much money does Andy make for each cake?"""
    ingredients_cost = 12
    packaging_cost = 1
    total_cost_per_cake = ingredients_cost / 2 + packaging_cost
    selling_price_per_cake = 15
    profit_per_cake = selling_price_per_cake - total_cost_per_cake
    result = profit_per_cake
    return result

print(solution())