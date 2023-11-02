def solution():
    
    adidas_price = 45
    nike_price = 60
    reebok_price = 35
    adidas_sold = 6
    nike_sold = 8
    reebok_sold = 9
    total_sales = adidas_sold * adidas_price + nike_sold * nike_price + reebok_sold * reebok_price
    difference = total_sales - 1000
    result = difference
    return result

print(solution())