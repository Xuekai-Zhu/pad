def solution():
    initial_price = 1000
    # Price after the first month
    price_after_first_month = initial_price - (initial_price * 0.1)
    # Price after the second month
    price_after_second_month = price_after_first_month - (price_after_first_month * 0.2)
    result = price_after_second_month
    return result

print(solution())