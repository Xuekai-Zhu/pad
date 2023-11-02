def solution():
    tissues_per_box = 160
    boxes_bought = 3
    tissues_used = 210
    tissues_left = tissues_per_box * boxes_bought - tissues_used
    result = tissues_left
    return result

print(solution())