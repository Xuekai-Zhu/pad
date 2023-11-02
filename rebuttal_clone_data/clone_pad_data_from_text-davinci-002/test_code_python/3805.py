def solution():
    hourly_rate = 70
    pounds_sold_1 = 5
    pounds_sold_2 = 7
    price_per_pound = 20
    total_price = (hourly_rate * 20) + (pounds_sold_1 * price_per_pound) + (pounds_sold_2 * price_per_pound)
    result = total_price
    return result

print(solution())