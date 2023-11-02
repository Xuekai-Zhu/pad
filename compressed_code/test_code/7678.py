def solution():
    
    first_stack = 7
    second_stack = first_stack + 5
    final_stack = second_stack + 7
    blocks_fallen = first_stack + (second_stack - 2) + (final_stack - 3)
    result = blocks_fallen
    return result

print(solution())