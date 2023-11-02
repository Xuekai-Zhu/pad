def solution():
    """Tom Sawyer has tricked his friends into whitewashing Aunt Polly's 100-foot fence. His first friend, Ben, whitewashed 10 feet. His second friend Billy whitewashed a fifth of the remaining fence. A third friend, Johnny, whitewashed a third of the fence that was left after that. How much of the fence still needs to be whitewashed?"""
    # Define the length of the fence
    fence_length = 100

    # Calculate the length of fence that Ben whitewashed
    ben_length = 10

    # Calculate the remaining length of fence after Ben whitewashed
    remaining_length = fence_length - ben_length

    # Calculate the length of fence that Billy whitewashed
    billy_length = remaining_length / 5

    # Calculate the remaining length of fence after Billy whitewashed
    remaining_length -= billy_length

    # Calculate the length of fence that Johnny whitewashed
    johnny_length = remaining_length / 3

    # Calculate the remaining length of fence after Johnny whitewashed
    remaining_length -= johnny_length

    # Return the length of fence that still needs to be whitewashed
    result = remaining_length
    return result

print(solution())