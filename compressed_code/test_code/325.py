def solution():
    
    total_bulbs = 40
    used_bulbs = 16
    remaining_bulbs = total_bulbs - used_bulbs
    friend_bulbs = remaining_bulbs / 2
    total_remaining = remaining_bulbs - friend_bulbs
    result = total_remaining
    return result

print(solution())