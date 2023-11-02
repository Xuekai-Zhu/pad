def solution():
    forward_steps = 3  # Jeffrey takes 3 steps forward
    backward_steps = 2  # Jeffrey takes 2 steps backward
    distance = 66  # The distance between the house and mailbox is 66 steps

    # Calculate the number of forward and backward steps Jeffrey needs to take
    forward_count = distance / (forward_steps - backward_steps)  # Each cycle of 3 steps forward and 2 steps backward covers a net distance of 1 step
    backward_count = forward_count * 2

    # Calculate the total number of steps Jeffrey takes
    total_steps = forward_count + backward_count
    result = total_steps
    return result

print(solution())