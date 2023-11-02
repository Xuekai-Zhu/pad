def solution():
    doughnuts_made = 300
    boxes_sold = 27
    doughnuts_per_box = 10
    doughnuts_left = doughnuts_made - (boxes_sold * doughnuts_per_box)
    result = doughnuts_left
    return result

print(solution())