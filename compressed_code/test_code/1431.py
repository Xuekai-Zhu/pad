def solution():
    
    total_hats = 3 * 15
    torn_hats = 5
    used_hats = 25
    unused_hats = total_hats - torn_hats - used_hats
    result = unused_hats
    return result

print(solution())