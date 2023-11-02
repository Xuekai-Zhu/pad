def solution():
    """Jess made 3 different stacks of wooden blocks. The first stack was 7 blocks high, the second stack was 5 block(s) higher than the first, and the final stack was 7 block(s) higher than the second. Jess’ little sister knocked over the entire first tower, in the second tower she left 2 blocks standing, and in the final tower she left 3 blocks standing. How many blocks in total fell down?"""
    first_stack_height = 7
    second_stack_height = first_stack_height + 5
    final_stack_height = second_stack_height + 7
    total_blocks_fell = first_stack_height + (second_stack_height-2) + (final_stack_height-3)
    result = total_blocks_fell
    return result

print(solution())