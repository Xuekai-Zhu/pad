def solution():
    
    left_knee_bandages = 2
    right_knee_bandages = 3
    total_bandages_used = left_knee_bandages + right_knee_bandages
    dozen_bandages = 24
    box_bandages = dozen_bandages - 8
    bandages_left = box_bandages - total_bandages_used
    result = bandages_left
    return result

print(solution())