def solution():
    """Donna cut her pizza into 12 slices and ate half for lunch. She ate 1/3 of the remaining pizza for dinner. How many slices are left for Donna's lunch tomorrow?"""
    total_slices = 12
    leftover_slices = total_slices / 2
    remaining_slices = leftover_slices - (leftover_slices / 3)
    result = remaining_slices
    return result

print(solution())