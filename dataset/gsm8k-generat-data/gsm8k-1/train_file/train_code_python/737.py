def solution():
    """Tom Sawyer has tricked his friends into whitewashing Aunt Polly's 100-foot fence. His first friend, Ben, whitewashed 10 feet. His second friend Billy whitewashed a fifth of the remaining fence. A third friend, Johnny, whitewashed a third of the fence that was left after that. How much of the fence still needs to be whitewashed?"""
    fence_length = 100
    ben_whitewash = 10
    remaining_fence = fence_length - ben_whitewash
    billy_whitewash = remaining_fence / 5
    remaining_fence -= billy_whitewash
    johnny_whitewash = remaining_fence / 3
    remaining_fence -= johnny_whitewash
    result = remaining_fence
    return result

print(solution())