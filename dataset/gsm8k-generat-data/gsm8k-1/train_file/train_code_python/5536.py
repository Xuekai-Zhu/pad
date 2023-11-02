def solution():
    """Cody has an insurance plan that will give him a discount if he logs a total of 100,000 steps. For the first week, he logs 1,000 steps a day. He increases his daily number of steps by 1,000 every week. After 4 weeks how far away from his step goal will he be?"""
    goal_steps = 100000
    starting_steps = 1000 * 7
    weekly_increase = 1000
    total_steps = starting_steps
    for i in range(2, 5):
        total_steps += (1000 * 7) + (i - 1) * weekly_increase * 7

    steps_away = goal_steps - total_steps
    result = steps_away
    return result

print(solution())