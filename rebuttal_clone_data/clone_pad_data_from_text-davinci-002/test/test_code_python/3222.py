def solution():
    bread_slices = 12
    breakfast_slices = bread_slices / 3
    lunch_slices = 2
    remaining_slices = bread_slices - breakfast_slices - lunch_slices
    result = remaining_slices
    return result

print(solution())