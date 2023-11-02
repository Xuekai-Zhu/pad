def solution():
    
    total_slices = 16
    slices_eaten_first_day = total_slices // 4
    slices_remaining_first_day = total_slices - slices_eaten_first_day
    slices_eaten_second_day = slices_remaining_first_day // 4
    slices_remaining_second_day = slices_remaining_first_day - slices_eaten_second_day - 4
    result = slices_remaining_second_day
    return result

print(solution())