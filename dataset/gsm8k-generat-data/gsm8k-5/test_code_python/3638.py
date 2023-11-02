def solution():
    # Calculate the total amount of money raised from selling pizzas
    pizza_sales = 15 * 12  # 15 boxes of pizza at $12 per box

    # Calculate the total amount of money raised from selling potato fries
    fries_sales = 40 * 0.3  # 40 packs of potato fries at $0.30 per pack

    # Calculate the total amount of money raised from selling soda
    soda_sales = 25 * 2  # 25 cans of soda at $2 per can

    # Calculate the total amount of money raised
    total_sales = pizza_sales + fries_sales + soda_sales

    # Calculate how much more money Einstein needs to raise to reach his goal
    remaining_amount = 500 - total_sales
    result = remaining_amount
    return result

print(solution())