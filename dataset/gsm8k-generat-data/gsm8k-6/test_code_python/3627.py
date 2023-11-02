def solution():
    # Calculate the total number of steps Jeffrey takes to get to the mailbox
    forward_steps = 3 * (66 // 5)  # Jeffrey takes three steps forward for every five steps taken
    backward_steps = 2 * (66 // 5)  # Jeffrey takes two steps backward for every five steps taken
    remaining_steps = 3 * (66 % 5)  # Jeffrey takes three steps forward for the remaining steps
    total_steps = forward_steps + backward_steps + remaining_steps
    result = total_steps
    return result

print(solution())