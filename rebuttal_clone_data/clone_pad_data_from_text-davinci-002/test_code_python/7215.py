def solution():
    daily_average_pastries = 20
    daily_average_bread = 10
    today_pastries = 14
    today_bread = 25
    price_pastries = 2
    price_bread = 4
    daily_average_sale = (daily_average_pastries * price_pastries) + (daily_average_bread * price_bread)
    today_sale = (today_pastries * price_pastries) + (today_bread * price_bread)
    difference = today_sale - daily_average_sale
    result = difference
    return result

print(solution())