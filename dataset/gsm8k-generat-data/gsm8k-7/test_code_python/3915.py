def solution():
    first_period_blocks = 4
    second_period_blocks = 2 * first_period_blocks
    third_period_blocks = second_period_blocks - 3

    total_blocks = 21
    fourth_period_blocks = total_blocks - first_period_blocks - second_period_blocks - third_period_blocks
    
    result = fourth_period_blocks
    return result

print(solution())