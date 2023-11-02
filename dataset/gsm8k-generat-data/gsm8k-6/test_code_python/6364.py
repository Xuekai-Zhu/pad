def solution():
    # Calculate the amount of money made from selling the treadmill
    treadmill_sale = 100

    # Calculate the amount of money made from selling the chest of drawers
    drawers_sale = treadmill_sale / 2

    # Calculate the amount of money made from selling the television
    tv_sale = treadmill_sale * 3

    # Calculate the total amount of money made from the three items
    total_sales = treadmill_sale + drawers_sale + tv_sale

    # Calculate the total amount of money made during the garage sale
    total_money = total_sales / 0.75

    result = total_money
    return result

print(solution())