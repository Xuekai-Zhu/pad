def solution():
    
    total_nails = 400
    used_kitchen = total_nails * 0.3
    remaining_nails = total_nails - used_kitchen
    used_fence = remaining_nails * 0.7
    remaining_nails -= used_fence
    result = remaining_nails
    return result

print(solution())