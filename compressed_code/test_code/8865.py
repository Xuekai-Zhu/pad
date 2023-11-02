def solution():
    
    slices_sold = 24
    pizzas_sold = 3
    price_per_slice = 3
    price_per_pizza = 15
    total_slices = slices_sold + (pizzas_sold * 8)  
    total_sales = (slices_sold * price_per_slice) + (pizzas_sold * price_per_pizza)
    result = total_sales
    return result

print(solution())