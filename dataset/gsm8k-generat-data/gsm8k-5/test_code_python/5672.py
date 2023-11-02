def solution():
    first_stack = 5  # The first stack was 5 blocks tall
    second_stack = first_stack + 2  # The second stack was 2 blocks taller than the first
    third_stack = second_stack - 5  # The third stack was 5 blocks shorter than the second
    fourth_stack = third_stack + 5  # The last stack was 5 blocks taller than the third
    total_blocks = first_stack + second_stack + third_stack + fourth_stack  # Calculate the total number of blocks

    result = total_blocks
    return result

print(solution())