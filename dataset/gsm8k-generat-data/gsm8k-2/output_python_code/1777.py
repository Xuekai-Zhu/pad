def solution():
    """Dorothy spent $53 to buy doughnut ingredients. If she made 25 doughnuts and sells each for $3, how much was her profit?"""
    ingredient_cost = 53
    doughnuts_made = 25
    doughnut_price = 3
    total_revenue = doughnuts_made * doughnut_price
    profit = total_revenue - ingredient_cost
    result = profit
    return result

print(solution())