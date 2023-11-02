def solution():
    
    first_stack = 5
    second_stack = first_stack + 2
    third_stack = second_stack - 5
    last_stack = third_stack + 5
    total_blocks = first_stack + second_stack + third_stack + last_stack
    result = total_blocks
    return result

print(solution())