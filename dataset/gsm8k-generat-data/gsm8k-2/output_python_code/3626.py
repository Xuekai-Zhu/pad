def solution():
    """When Jeffrey walks, for every three steps forward, he takes two steps backwards. Therefore, if the distance between the house and the mailbox is 66 steps, what is the total number of steps Jeffrey takes when he goes from the house to the mailbox?"""
    forward_steps = 3
    backward_steps = 2
    distance = 66
    total_steps = 0
    while distance > 0:
        if distance >= forward_steps:
            total_steps += forward_steps
            distance -= forward_steps
        else:
            total_steps += distance
            distance = 0
        if distance >= backward_steps:
            distance -= backward_steps
            total_steps += backward_steps
    result = total_steps
    return result

print(solution())