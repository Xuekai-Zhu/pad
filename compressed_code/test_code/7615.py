def solution():
    
    bandages_left = 0
    bandages_used = 2 + 3
    dozen_bandages = 24
    box_bandages = dozen_bandages - 8
    bandages_left = box_bandages - bandages_used
    result = bandages_left
    return result

print(solution())