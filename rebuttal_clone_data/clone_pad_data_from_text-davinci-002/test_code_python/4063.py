def solution():
    big_stack = 5
    short_stack = 3
    big_stack_orders = 6
    short_stack_orders = 9
    total_pancakes = short_stack_orders * short_stack + big_stack_orders * big_stack
    result = total_pancakes
    return result

print(solution())