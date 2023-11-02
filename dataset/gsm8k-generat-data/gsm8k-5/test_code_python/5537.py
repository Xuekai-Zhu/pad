def solution():
    goal = 100000  # Cody's step goal
    total_steps = 0  # Total number of steps logged by Cody
    steps_per_day = 1000  # Cody logs 1000 steps on the first day
    increase_per_week = 1000  # Cody increases his steps by 1000 every week

    # Calculate the total number of steps logged by Cody
    for i in range(4):
        total_steps += (steps_per_day * 7)
        steps_per_day += increase_per_week

    # Calculate how far away Cody is from his step goal
    steps_left = goal - total_steps
    result = steps_left
    return result

print(solution())