def solution():
    """Tom Sawyer has tricked his friends into whitewashing Aunt Polly's 100-foot fence. His first friend, Ben, whitewashed 10 feet. His second friend Billy whitewashed a fifth of the remaining fence. A third friend, Johnny, whitewashed a third of the fence that was left after that. How much of the fence still needs to be whitewashed?"""
    total_fence = 100
    ben_fence = 10
    remaining_fence = total_fence - ben_fence
    billy_fence = remaining_fence * (1/5)
    remaining_fence -= billy_fence
    johnny_fence = remaining_fence * (1/3)
    remaining_fence -= johnny_fence
    result = remaining_fence
    return result

print(solution())