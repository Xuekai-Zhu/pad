def solution():
    forward_steps = 3
    backward_steps = 2
    total_distance = 66

    # Calculate the number of "sets" of three forward steps and two backward steps Jeffrey must take
    sets_needed = total_distance / (forward_steps - backward_steps)

    # Calculate the total number of steps Jeffrey takes, including the extra forward steps at the end
    total_steps = sets_needed * (forward_steps + backward_steps) + forward_steps
    result = total_steps
    return result

print(solution())