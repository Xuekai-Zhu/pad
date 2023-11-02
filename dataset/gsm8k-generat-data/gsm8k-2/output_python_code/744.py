def solution():
    """Village Foods sells good food at a fair price. Their specialty is fresh vegetables. If they get 500 customers per month, and each customer purchases 2 heads of lettuce for $1 each and 4 tomatoes for $0.5 apiece, then how much money, in dollars, will the store receive in sales of lettuce and tomatoes per month?"""
    num_customers = 500
    num_lettuce = 2
    lettuce_price = 1
    num_tomatoes = 4
    tomato_price = 0.5
    total_lettuce_price = num_customers * num_lettuce * lettuce_price
    total_tomato_price = num_customers * num_tomatoes * tomato_price
    total_sales = total_lettuce_price + total_tomato_price
    result = total_sales
    return result

print(solution())