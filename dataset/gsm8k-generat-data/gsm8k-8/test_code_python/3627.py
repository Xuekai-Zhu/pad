def solution():
    # Calculate the number of steps Jeffrey takes for every 5 steps
    steps_per_5 = 3 - 2

    # Calculate the number of times Jeffrey needs to take 5 steps to reach the mailbox
    num_5_steps = 66 // 5

    # Calculate the total number of steps Jeffrey takes
    total_steps = num_5_steps * steps_per_5 + (66 % 5) * 3
    result = total_steps
    return result

print(solution())