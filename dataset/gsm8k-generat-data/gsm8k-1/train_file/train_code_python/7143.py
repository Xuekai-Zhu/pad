def solution():
    """The price of an iPhone fell 10% in a particular month and another 20% in the second month. If the initial price was $1000, calculate the price after the second month."""
    initial_price = 1000
    first_month_discount = 0.1
    second_month_discount = 0.2
    price_after_first_month = initial_price * (1 - first_month_discount)
    price_after_second_month = price_after_first_month * (1 - second_month_discount)
    result = price_after_second_month
    return result

print(solution())