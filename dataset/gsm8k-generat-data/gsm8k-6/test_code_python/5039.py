def solution():
    # Calculate the total revenue from selling small and large pizzas
    small_pizza_revenue = 2 * 8  # 8 small pizzas were sold for $2 each
    total_revenue = 40  
    large_pizza_revenue = total_revenue - small_pizza_revenue  # Subtract the revenue from selling small pizzas

    # Calculate the number of large pizzas sold
    num_large_pizzas = large_pizza_revenue // 8  # Each large pizza is sold for $8
    result = num_large_pizzas
    return result

print(solution())