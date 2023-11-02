def solution():
    initial_price = 1000  # initial price of the iPhone
    after_first_month = initial_price - (0.1 * initial_price)  # price after 10% discount in first month
    after_second_month = after_first_month - (0.2 * after_first_month)  # price after 20% discount in second month
    result = after_second_month
    return result

print(solution())