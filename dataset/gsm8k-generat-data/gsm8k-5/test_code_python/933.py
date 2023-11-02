def solution():
    first_staircase = 20  # First staircase has 20 steps
    second_staircase = 2 * first_staircase  # Second staircase has twice as many steps as the first
    third_staircase = second_staircase - 10  # Third staircase has 10 fewer steps than the second
    step_length = 0.5  # Each step is 0.5 feet long

    # Calculate the total distance climbed
    total_distance = (first_staircase + second_staircase + third_staircase) * step_length
    result = total_distance
    return result

print(solution())