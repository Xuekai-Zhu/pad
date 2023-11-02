def solution():
    
    pies_baked = 200
    price_per_pie = 20
    sales = pies_baked * price_per_pie
    ingredient_cost = (3/5) * sales
    profit = sales - ingredient_cost
    result = profit
    return result

print(solution())