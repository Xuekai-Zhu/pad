def solution():
    
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