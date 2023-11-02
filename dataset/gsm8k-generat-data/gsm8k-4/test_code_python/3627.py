def solution():
    """When Jeffrey walks, for every three steps forward, he takes two steps backwards. Therefore, if the distance between the house and the mailbox is 66 steps, what is the total number of steps Jeffrey takes when he goes from the house to the mailbox?"""
    # Define the distance between the house and the mailbox
    distance = 66

    # Calculate the total number of steps Jeffrey takes to go from the house to the mailbox
    total_steps = distance * 5 / 3

    # round up the total number of steps to the nearest integer
    result = round(total_steps)
    return result

print(solution())