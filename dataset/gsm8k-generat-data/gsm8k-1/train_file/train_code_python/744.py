def solution():
    """Village Foods sells good food at a fair price. Their specialty is fresh vegetables. If they get 500 customers per month, and each customer purchases 2 heads of lettuce for $1 each and 4 tomatoes for $0.5 apiece, then how much money, in dollars, will the store receive in sales of lettuce and tomatoes per month?"""
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