def solution():
    
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