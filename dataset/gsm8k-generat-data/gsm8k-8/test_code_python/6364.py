def solution():
    # Calculate the amount earned from selling the treadmill
    treadmill_sale = 100

    # Calculate the amount earned from selling the chest of drawers
    drawers_sale = treadmill_sale / 2

    # Calculate the amount earned from selling the television
    tv_sale = treadmill_sale * 3

    # Calculate the total amount earned from selling these three items
    total_sales = treadmill_sale + drawers_sale + tv_sale

    # Calculate the total amount earned from the entire garage sale
    total_garage_sale = total_sales / 0.75

    result = total_garage_sale
    return result

print(solution())