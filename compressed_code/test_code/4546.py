def solution():
    
    first_stack = 7
    second_stack = first_stack + 3
    third_stack = second_stack - 6
    fourth_stack = third_stack + 10
    fifth_stack = 2 * second_stack
    total_blocks = first_stack + second_stack + third_stack + fourth_stack + fifth_stack
    result = total_blocks
    return result

print(solution())