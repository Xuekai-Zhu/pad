def solution():
    num_pies = 200
    price_per_pie = 20
    ingredient_frac = 3 / 5

    # Calculate the total revenue from selling all meat pies
    total_revenue = num_pies * price_per_pie

    # Calculate the amount of money set aside for buying ingredients
    ingredient_cost = total_revenue * ingredient_frac

    # Calculate the amount of money remaining after buying ingredients
    remaining_money = total_revenue - ingredient_cost
    result = remaining_money
    return result

print(solution())