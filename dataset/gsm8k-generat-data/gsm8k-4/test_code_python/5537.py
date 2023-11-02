def solution():
    """Cody has an insurance plan that will give him a discount if he logs a total of 100,000 steps. For the first week, he logs 1,000 steps a day. He increases his daily number of steps by 1,000 every week. After 4 weeks how far away from his step goal will he be?"""
    # Define Cody's step goal and the number of weeks he logged steps
    step_goal = 100000
    weeks = 4

    # Initialize the total number of steps logged
    total_steps = 0

    # Calculate the number of steps logged each week and add it to the total
    for i in range(1, weeks+1):
        steps_per_day = 1000 + 1000*(i-1)
        week_steps = steps_per_day * 7
        total_steps += week_steps

    # Calculate the difference between Cody's total steps and his step goal
    difference = step_goal - total_steps

    # Return the result
    result = difference
    return result

print(solution())