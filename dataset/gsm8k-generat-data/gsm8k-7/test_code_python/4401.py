def solution():
    nike_price = 60
    adidas_price = 45
    reebok_price = 35

    nike_sold = 8
    adidas_sold = 6
    reebok_sold = 9

    # Calculate the total amount of money from each brand sold
    total_nike_sales = nike_price * nike_sold
    total_adidas_sales = adidas_price * adidas_sold
    total_reebok_sales = reebok_price * reebok_sold

    # Calculate the total amount of money from all sales
    total_sales = total_nike_sales + total_adidas_sales + total_reebok_sales

    # Calculate the difference between the total sales and the quota
    difference = total_sales - 1000

    result = difference
    return result

print(solution())