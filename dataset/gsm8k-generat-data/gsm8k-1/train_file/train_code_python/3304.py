def solution():
    """Du Chin bakes 200 meat pies in a day. He sells them for $20 each and uses 3/5 of the sales to buy ingredients to make meat pies for sale on the next day. How much money does Du Chin remain with after setting aside the money for buying ingredients?"""
    pies_baked = 200
    price_per_pie = 20
    sales = pies_baked * price_per_pie
    ingredient_cost = (3/5) * sales
    profit = sales - ingredient_cost
    result = profit
    return result

print(solution())