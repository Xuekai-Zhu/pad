def solution():
    # Calculate the amount earned from selling the treadmill
    treadmill_price = 100
    total_sales_money = treadmill_price / 0.75

    # Calculate the amount earned from selling the chest of drawers
    chest_of_drawers_price = treadmill_price / 2
    total_sales_money += chest_of_drawers_price / 0.75

    # Calculate the amount earned from selling the television
    television_price = treadmill_price * 3
    total_sales_money += television_price / 0.75

    result = total_sales_money
    return result

print(solution())