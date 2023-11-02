def solution():
    fence_length = 100  # Aunt Polly's fence is 100 feet long

    # Ben whitewashes 10 feet of the fence
    fence_length -= 10

    # Billy whitewashes a fifth of the remaining fence
    fence_length *= 4/5

    # Johnny whitewashes a third of the fence that was left after Billy
    fence_length *= 2/3

    # Calculate how much of the fence still needs to be whitewashed
    still_needs_whitewash = fence_length
    result = still_needs_whitewash
    return result

print(solution())