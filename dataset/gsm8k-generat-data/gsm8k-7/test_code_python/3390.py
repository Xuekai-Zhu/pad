def solution():
    price_per_pizza = 5
    
    # Calculate the total cost of the triple cheese pizzas using the buy-1-get-1-free special
    num_triple_cheese_pizzas = 10
    num_free_triple_cheese_pizzas = num_triple_cheese_pizzas // 2
    total_triple_cheese_cost = (num_triple_cheese_pizzas - num_free_triple_cheese_pizzas) * price_per_pizza
    
    # Calculate the total cost of the meat lovers pizzas using the buy-2-get-1-free special
    num_meat_lovers_pizzas = 9
    num_free_meat_lovers_pizzas = num_meat_lovers_pizzas // 3
    total_meat_lovers_cost = (num_meat_lovers_pizzas - num_free_meat_lovers_pizzas) * price_per_pizza
    
    # Calculate the total cost of all pizzas
    total_cost = total_triple_cheese_cost + total_meat_lovers_cost
    result = total_cost
    return result

print(solution())