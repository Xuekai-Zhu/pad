def solution():
    # Define the number of pancakes in a big stack and a short stack
    big_stack = 5
    short_stack = 3

    # Calculate the total number of pancakes needed for the big stacks
    total_big_stack = big_stack * 6

    # Calculate the total number of pancakes needed for the short stacks
    total_short_stack = short_stack * 9

    # Calculate the total number of pancakes needed
    total_pancakes = total_big_stack + total_short_stack
    result = total_pancakes
    return result

print(solution())