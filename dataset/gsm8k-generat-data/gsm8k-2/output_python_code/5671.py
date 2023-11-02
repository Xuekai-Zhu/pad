def solution():
    """Pablo made 4 stacks of toy blocks. The first stack was 5 blocks tall. The second stack was 2 blocks taller than the first. The third stack was 5 blocks shorter than the second stack, and the last stack was 5 blocks taller than the third stack. How many toy blocks did Pablo use in all?"""
    first_stack = 5
    second_stack = first_stack + 2
    third_stack = second_stack - 5
    last_stack = third_stack + 5
    total_blocks = first_stack + second_stack + third_stack + last_stack
    result = total_blocks
    return result

print(solution())