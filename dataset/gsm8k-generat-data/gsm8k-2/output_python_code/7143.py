def solution():
    """The price of an iPhone fell 10% in a particular month and another 20% in the second month. If the initial price was $1000, calculate the price after the second month."""
    initial_price = 1000
    first_month_price = initial_price * 0.9
    second_month_price = first_month_price * 0.8
    result = second_month_price
    return result

print(solution())