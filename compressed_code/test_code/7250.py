def solution():
    
    hats_per_bag = 15
    total_hats = hats_per_bag * 3
    torn_hats = 5
    used_hats = 25
    unused_hats = total_hats - torn_hats - used_hats
    result = unused_hats
    return result

print(solution())