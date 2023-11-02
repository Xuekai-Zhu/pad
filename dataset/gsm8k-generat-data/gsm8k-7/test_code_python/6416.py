def solution():
    steps_back1 = 5
    steps_forward1 = 10
    steps_back2 = 2
    double_forward = steps_back2 * 2

    # Calculate the net steps backward
    net_steps_back = steps_back1 + steps_back2

    # Calculate the net steps forward
    net_steps_forward = steps_forward1 + double_forward

    # Calculate the final number of steps forward from Frank's original position
    steps_forward = net_steps_forward - net_steps_back
    result = steps_forward
    return result

print(solution())