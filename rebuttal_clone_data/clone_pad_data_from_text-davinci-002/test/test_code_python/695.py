def solution():
    apples_sold_morning = 40
    oranges_sold_morning = 30
    apples_sold_afternoon = 50
    oranges_sold_afternoon = 40
    apple_price = 1.50
    orange_price = 1
    sales_morning = (apples_sold_morning * apple_price) + (oranges_sold_morning * orange_price)
    sales_afternoon = (apples_sold_afternoon * apple_price) + (oranges_sold_afternoon * orange_price)
    total_sales = sales_morning + sales_afternoon
    result = total_sales
    return result

print(solution())