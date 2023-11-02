def solution():
    num_short_stack = 9
    num_big_stack = 6

    # Calculate the total number of short stack pancakes needed
    total_short_stack = num_short_stack * 3

    # Calculate the total number of big stack pancakes needed
    total_big_stack = num_big_stack * 5

    # Calculate the total number of pancakes Hank needs to make
    total_pancakes = total_short_stack + total_big_stack
    result = total_pancakes
    return result

print(solution())