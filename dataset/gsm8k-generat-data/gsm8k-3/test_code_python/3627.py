def solution():
    """When Jeffrey walks, for every three steps forward, he takes two steps backwards.  Therefore, if the distance between the house and the mailbox is 66 steps, what is the total number of steps Jeffrey takes when he goes from the house to the mailbox?"""
    # Define the number of steps forward and backward for each cycle
    forward_steps = 3
    backward_steps = 2

    # Define the distance between the house and the mailbox
    distance = 66

    # Calculate the number of forward-backward cycles Jeffrey needs to complete
    cycles = distance // (forward_steps + backward_steps)

    # Calculate the total number of steps Jeffrey takes
    total_steps = cycles * (forward_steps + backward_steps) + distance % (forward_steps + backward_steps)

    # Display the total number of steps Jeffrey takes
    result = total_steps
    return result

print(solution())