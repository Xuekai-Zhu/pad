def solution():
    adidas_price = 45
    nike_price = 60
    reebok_price = 35

    adidas_sold = 6
    nike_sold = 8
    reebok_sold = 9

    total_sales = (adidas_price * adidas_sold) + (nike_price * nike_sold) + (reebok_price * reebok_sold)

    shortfall = 1000 - total_sales

    result = shortfall
    return result

print(solution())