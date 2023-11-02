def solution():
    
    total_slices = 2 * 8
    friend_slices = total_slices // 4
    remaining_slices = total_slices - friend_slices
    family_slices = remaining_slices // 3
    remaining_slices -= family_slices
    remaining_slices -= 3 
    result = remaining_slices
    return result

print(solution())