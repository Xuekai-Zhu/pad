def solution():
    
    total_nails = 400
    kitchen_nails = total_nails * 0.3
    remaining_nails = total_nails - kitchen_nails
    fence_nails = remaining_nails * 0.7
    remaining_nails = remaining_nails - fence_nails
    result = remaining_nails
    return result

print(solution())