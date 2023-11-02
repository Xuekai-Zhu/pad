def solution():
    """Pablo made 4 stacks of toy blocks. The first stack was 5 blocks tall. The second stack was 2 blocks taller than the first. The third stack was 5 blocks shorter than the second stack, and the last stack was 5 blocks taller than the third stack. How many toy blocks did Pablo use in all?"""
    # Define the height of the first stack
    first_stack_height = 5

    # Define the height of the second stack
    second_stack_height = first_stack_height + 2

    # Define the height of the third stack
    third_stack_height = second_stack_height - 5

    # Define the height of the fourth (last) stack
    fourth_stack_height = third_stack_height + 5

    # Calculate the total number of blocks used
    total_blocks = first_stack_height + second_stack_height + third_stack_height + fourth_stack_height

    # Display the total number of blocks used
    result = total_blocks
    return result

print(solution())