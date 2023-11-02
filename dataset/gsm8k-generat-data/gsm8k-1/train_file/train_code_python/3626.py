def solution():
    """When Jeffrey walks, for every three steps forward, he takes two steps backwards. Therefore, if the distance between the house and the mailbox is 66 steps, what is the total number of steps Jeffrey takes when he goes from the house to the mailbox?"""
    forward_steps = 3
    backward_steps = 2
    distance = 66
    total_steps = (forward_steps + backward_steps) * (distance // forward_steps)
    result = total_steps
    return result

print(solution())