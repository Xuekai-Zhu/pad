def solution():
    first_staircase_steps = 20
    second_staircase_steps = 2 * first_staircase_steps
    third_staircase_steps = second_staircase_steps - 10
    feet_per_step = 0.5
    total_feet = first_staircase_steps * feet_per_step + second_staircase_steps * feet_per_step + third_staircase_steps * feet_per_step
    result = total_feet
    
    return result

print(solution())