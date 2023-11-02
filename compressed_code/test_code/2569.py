def solution():
    
    pies_baked = 200
    price_per_pie = 20
    total_sales = pies_baked * price_per_pie
    ingredients_cost = 0.6 * total_sales
    remaining_money = total_sales - ingredients_cost
    result = remaining_money
    return result

print(solution())