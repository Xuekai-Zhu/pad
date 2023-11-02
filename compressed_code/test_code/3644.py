def solution():
    
    chips_per_bag = 81
    chips_per_cookie = 9
    cookies_per_batch = chips_per_bag // (chips_per_cookie * 3)
    result = cookies_per_batch
    return result

print(solution())