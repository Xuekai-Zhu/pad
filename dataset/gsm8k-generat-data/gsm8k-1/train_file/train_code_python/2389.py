def solution():
    """Jess made 3 different stacks of wooden blocks. The first stack was 7 blocks high, the second stack was 5 block(s) higher than the first, and the final stack was 7 block(s) higher than the second. Jess’ little sister knocked over the entire first tower, in the second tower she left 2 blocks standing, and in the final tower she left 3 blocks standing. How many blocks in total fell down?"""
    first_stack = 7
    second_stack = first_stack + 5
    final_stack = second_stack + 7
    blocks_fallen = first_stack + (second_stack - 2) + (final_stack - 3)
    result = blocks_fallen
    return result

print(solution())