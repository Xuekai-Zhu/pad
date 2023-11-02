def solution():
    """Thomas made 4 stacks of wooden blocks. The first stack was 7 blocks tall. The second stack was 3 blocks taller than the first. The third stack was 6 blocks shorter than the second stack, and the fourth stack was 10 blocks taller than the third stack. If the fifth stack has twice as many blocks as the second stack, how many blocks did Thomas use in all?"""
    first_stack = 7
    second_stack = first_stack + 3
    third_stack = second_stack - 6
    fourth_stack = third_stack + 10
    fifth_stack = 2 * second_stack
    total_blocks = first_stack + second_stack + third_stack + fourth_stack + fifth_stack
    result = total_blocks
    return result

print(solution())