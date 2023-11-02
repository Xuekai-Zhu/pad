def solution():
    
    step_goal = 100000
    total_steps = 0
    for i in range(1, 5):
        total_steps += (i * 1000) * 7
    steps_away = step_goal - total_steps
    result = abs(steps_away)
    return result

print(solution())