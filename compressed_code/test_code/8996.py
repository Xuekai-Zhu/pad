def solution():
    
    big_stack = 5
    short_stack = 3
    num_big_stack_orders = 6
    num_short_stack_orders = 9
    total_pancakes_needed = (big_stack * num_big_stack_orders) + (short_stack * num_short_stack_orders)
    result = total_pancakes_needed
    return result

print(solution())