def solution():
    # Calculate the total number of pancakes needed for short stack orders
    short_stack_pancakes = 3 * 9  # 9 customers order short stack pancakes, each with 3 pancakes
    # Calculate the total number of pancakes needed for big stack orders
    big_stack_pancakes = 5 * 6  # 6 customers order big stack pancakes, each with 5 pancakes
    # Calculate the total number of pancakes needed
    total_pancakes = short_stack_pancakes + big_stack_pancakes
    result = total_pancakes
    return result

print(solution())