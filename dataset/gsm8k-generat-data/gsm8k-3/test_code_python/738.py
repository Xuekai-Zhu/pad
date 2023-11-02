def solution():
    """Tom Sawyer has tricked his friends into whitewashing Aunt Polly's 100-foot fence. His first friend, Ben, whitewashed 10 feet. His second friend Billy whitewashed a fifth of the remaining fence. A third friend, Johnny, whitewashed a third of the fence that was left after that. How much of the fence still needs to be whitewashed?"""
    # Define the length of the fence
    fence_length = 100

    # First friend whitewashed 10 feet
    remaining_length = fence_length - 10

    # Second friend whitewashed a fifth of the remaining fence
    remaining_length = remaining_length - (remaining_length / 5)

    # Third friend whitewashed a third of the remaining fence
    remaining_length = remaining_length - (remaining_length / 3)

    # Display the remaining length of the fence to be whitewashed
    result = remaining_length
    return result

print(solution())