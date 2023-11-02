def solution():
    old_price = 85
    new_price = 102

    # Calculate the difference in price
    price_diff = new_price - old_price

    # Calculate the percent increase
    percent_increase = (price_diff / old_price) * 100

    result = percent_increase
    return result

print(solution())