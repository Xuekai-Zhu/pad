def solution():
    """Dorothy spent $53 to buy doughnut ingredients. If she made 25 doughnuts and sells each for $3, how much was her profit?"""
    cost_of_ingredients = 53
    number_of_doughnuts = 25
    price_per_doughnut = 3
    total_revenue = number_of_doughnuts * price_per_doughnut
    profit = total_revenue - cost_of_ingredients
    result = profit
    return result

print(solution())