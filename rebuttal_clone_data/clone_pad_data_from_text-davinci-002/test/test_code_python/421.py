def solution():
     initial_fence = 100
     fence_painted = 10
     fence_remaining = initial_fence - fence_painted
     fence_painted = fence_remaining / 5
     fence_remaining = fence_remaining - fence_painted
     fence_painted = fence_remaining / 3
     fence_remaining = fence_remaining - fence_painted
     result = fence_remaining
     return result

print(solution())