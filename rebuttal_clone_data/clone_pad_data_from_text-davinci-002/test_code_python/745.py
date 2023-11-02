def solution():
     customers_per_month = 500
     lettuce_per_customer = 2
     tomato_per_customer = 4
     lettuce_price = 1
     tomato_price = 0.5
     lettuce_sales = customers_per_month * lettuce_per_customer * lettuce_price
     tomato_sales = customers_per_month * tomato_per_customer * tomato_price
     total_sales = lettuce_sales + tomato_sales
     result = total_sales
     return result

print(solution())