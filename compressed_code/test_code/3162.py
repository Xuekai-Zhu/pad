def solution():
    
    short_stack = 3
    big_stack = 5
    num_short_stack_orders = 9
    num_big_stack_orders = 6
    total_short_pancakes = short_stack * num_short_stack_orders
    total_big_pancakes = big_stack * num_big_stack_orders
    total_pancakes = total_short_pancakes + total_big_pancakes
    result = total_pancakes
    return result

print(solution())