def solution():
    bottles_sold_morning = 55
    bottles_sold_evening = bottles_sold_morning - 6
    price_per_bottle = 0.50
    total_sales_morning = bottles_sold_morning * price_per_bottle
    total_sales_evening = bottles_sold_evening * price_per_bottle
    difference_in_sales = total_sales_evening - total_sales_morning
    result = difference_in_sales
    return result

print(solution())