def solution():
    
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