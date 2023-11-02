def solution():
    
    apple_slices_per_pie = 8
    peach_slices_per_pie = 6
    total_apple_slices = 56
    total_peach_slices = 48
    total_apple_pies = total_apple_slices / apple_slices_per_pie
    total_peach_pies = total_peach_slices / peach_slices_per_pie
    total_pies = total_apple_pies + total_peach_pies
    result = total_pies
    return result

print(solution())