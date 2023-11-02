def solution():
    
    first_stack_height = 7
    second_stack_height = first_stack_height + 5
    final_stack_height = second_stack_height + 7
    total_blocks_fell = first_stack_height + (second_stack_height-2) + (final_stack_height-3)
    result = total_blocks_fell
    return result

print(solution())