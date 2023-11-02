def solution():
    """Cody has an insurance plan that will give him a discount if he logs a total of 100,000 steps. For the first week, he logs 1,000 steps a day. He increases his daily number of steps by 1,000 every week. After 4 weeks how far away from his step goal will he be?"""
    step_goal = 100000
    total_steps = 0
    for i in range(1, 5):
        total_steps += (i * 1000) * 7
    steps_away = step_goal - total_steps
    result = abs(steps_away)
    return result

print(solution())