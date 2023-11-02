def solution():
    dish_prices = [10, 13, 17]
    tip_percentage = 0.1  # 10% tip

    # Calculate the total cost of all dishes
    total_cost = sum(dish_prices)

    # Calculate the amount of the tip
    tip_amount = total_cost * tip_percentage

    result = tip_amount
    return result

print(solution())