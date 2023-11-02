def solution():
    total_items = 13
    num_pens = total_items / 3 * 2
    num_pencils = total_items - num_pens - 1
    result = num_pencils
    return result

print(solution())