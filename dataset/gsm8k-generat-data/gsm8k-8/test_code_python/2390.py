def solution():
    # Define the height of the first stack
    first_stack = 7

    # Define the height of the second stack
    second_stack = first_stack + 5

    # Define the height of the third stack
    third_stack = second_stack + 7

    # Define the number of blocks left standing in each stack
    first_standing = 0
    second_standing = 2
    third_standing = 3

    # Calculate the number of blocks that fell down
    first_fell = first_stack - first_standing
    second_fell = second_stack - second_standing
    third_fell = third_stack - third_standing

    # Calculate the total number of blocks that fell down
    total_fell = first_fell + second_fell + third_fell

    result = total_fell
    return result

print(solution())