def solution():
    # Calculate the height of the second stack
    second_stack_height = 7 + 5

    # Calculate the height of the final stack
    final_stack_height = second_stack_height + 7

    # Calculate the total number of blocks in all three stacks
    total_blocks = (7 + second_stack_height + final_stack_height)

    # Calculate the number of blocks knocked down in the first, second, and final towers
    blocks_knocked_down = (7 + (second_stack_height - 2) + (final_stack_height - 3))

    # Calculate the total number of blocks that fell down
    blocks_fell_down = total_blocks - (7 + (second_stack_height - 2) + (final_stack_height - 3))

    result = blocks_fell_down
    return result

print(solution())