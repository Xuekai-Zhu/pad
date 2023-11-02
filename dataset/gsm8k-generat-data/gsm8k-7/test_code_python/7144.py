def solution():
    initial_price = 1000
    first_month_discount = 0.1  # 10% discount
    second_month_discount = 0.2  # 20% discount

    # Calculate the price after the first month discount
    price_after_first_month = initial_price * (1 - first_month_discount)

    # Calculate the price after the second month discount
    price_after_second_month = price_after_first_month * (1 - second_month_discount)
    result = price_after_second_month
    return result

print(solution())