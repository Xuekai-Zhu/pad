def solution():
    
    total_bulbs = 40
    used_bulbs = 16
    remaining_bulbs = total_bulbs - used_bulbs
    friend_bulbs = remaining_bulbs / 2
    bulbs_left = remaining_bulbs - friend_bulbs
    result = bulbs_left
    return result

print(solution())