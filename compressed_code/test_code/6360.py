def solution():
    
    customers_per_month = 500
    lettuce_price = 1
    tomatoes_price = 0.5
    lettuce_per_customer = 2
    tomatoes_per_customer = 4
    lettuce_sales = customers_per_month * lettuce_per_customer * lettuce_price
    tomatoes_sales = customers_per_month * tomatoes_per_customer * tomatoes_price
    total_sales = lettuce_sales + tomatoes_sales
    result = total_sales
    return result

print(solution())