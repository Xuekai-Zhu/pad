def solution():
    # Calculate the total sales of the meat pies
    total_sales = 200 * 20  # Du Chin sells 200 meat pies for $20 each

    # Calculate the amount of money used to buy ingredients
    ingredient_cost = (3/5) * total_sales

    # Calculate the amount of money remaining after buying ingredients
    remaining_money = total_sales - ingredient_cost
    result = remaining_money
    return result

print(solution())