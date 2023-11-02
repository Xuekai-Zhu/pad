def solution():
    # Calculate the total amount of money earned from selling the meat pies
    total_earnings = 200 * 20

    # Calculate the amount of money used to buy ingredients
    ingredient_cost = total_earnings * (3/5)

    # Calculate the amount of money left over after buying ingredients
    remaining_money = total_earnings - ingredient_cost
    result = remaining_money
    return result

print(solution())