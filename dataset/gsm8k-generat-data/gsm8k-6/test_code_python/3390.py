def solution():
    # Calculate the total cost of the triple cheese pizzas using the buy-1-get-1-free special
    triple_cheese_cost = ((10 // 2) + (10 % 2)) * 5  # buy-1-get-1-free special
    # Calculate the total cost of the meat lovers pizzas using the buy-2-get-1-free special
    meat_lovers_cost = ((9 // 3) * 2 + (9 % 3)) * 5  # buy-2-get-1-free special
    # Calculate the total cost of all the pizzas
    total_cost = triple_cheese_cost + meat_lovers_cost
    result = total_cost
    return result

print(solution())