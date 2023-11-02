def solution():
    old_price = 85
    new_price = 102

    # Calculate the percent increase in price
    percent_increase = ((new_price - old_price) / old_price) * 100
    result = percent_increase
    return result

print(solution())