def solution():
    slices_toast = 10
    slices_leftover = 1
    toast_per_slice = 2
    original_slices = (slices_toast * toast_per_slice) + slices_leftover + 3
    result = original_slices
    return result

print(solution())