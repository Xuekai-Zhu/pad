def solution():
    """John climbs 3 staircases. The first staircase has 20 steps. The next has twice as many steps as the first. The final staircase has 10 fewer steps than the second one. Each step is 0.5 feet. How many feet did he climb?"""
    first_staircase = 20
    second_staircase = first_staircase * 2
    third_staircase = second_staircase - 10
    step_size = 0.5
    total_steps = first_staircase + second_staircase + third_staircase
    total_feet = total_steps * step_size
    result = total_feet
    return result

print(solution())