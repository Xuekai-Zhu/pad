def solution():
    # Define variables
    back1 = 5
    forward1 = 10
    back2 = 2
    forward2 = back2 * 2

    # Calculate total steps forward
    total_forward = forward1 + forward2

    # Calculate net steps forward
    net_forward = total_forward - back1

    result = net_forward
    return result

print(solution())