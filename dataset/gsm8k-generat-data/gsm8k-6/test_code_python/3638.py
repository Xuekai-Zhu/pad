def solution():
    # Calculate the total amount raised by Einstein
    pizza_sales = 15 * 12
    fries_sales = 40 * 0.30
    soda_sales = 25 * 2
    total_sales = pizza_sales + fries_sales + soda_sales

    # Calculate how much more money Einstein needs to raise
    remaining_amount = 500 - total_sales
    result = remaining_amount
    return result

print(solution())