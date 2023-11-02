def solution():
    # Calculate the total number of steps logged in 4 weeks
    total_steps = 0
    for i in range(4):
        total_steps += (i+1)*1000  # increase in steps by 1000 every week
    steps_left = 100000 - total_steps  # calculate how many steps are left to reach the goal
    result = steps_left
    return result

print(solution())