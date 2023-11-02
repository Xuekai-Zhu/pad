def solution():
    
    total_acres = 8
    riding_mower_percentage = 0.75
    push_mower_percentage = 0.25
    riding_mower_acres = total_acres * riding_mower_percentage
    push_mower_acres = total_acres * push_mower_percentage
    riding_mower_time = riding_mower_acres / 2
    push_mower_time = push_mower_acres / 1
    total_time = riding_mower_time + push_mower_time
    result = total_time
    return result

print(solution())