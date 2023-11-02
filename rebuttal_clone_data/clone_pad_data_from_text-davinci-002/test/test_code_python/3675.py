def solution():
    distance = 900
    distance_with_fence = distance - 42
    fence_length = 6
    fence_posts = distance_with_fence // fence_length
    total_posts = fence_posts * 2
    result = total_posts
    
    return result

print(solution())