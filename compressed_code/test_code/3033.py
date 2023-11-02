def solution():
    
    num_classes = 6
    folders_cost = 6
    pencils_cost = 2
    erasers_cost = 1

    num_folders = num_classes
    num_pencils = num_classes * 3
    num_erasers = num_pencils // 6

    total_cost = (num_folders * folders_cost) + (num_pencils * pencils_cost) + (num_erasers * erasers_cost)
    paint_cost = 80 - total_cost

    result = paint_cost
    return result

print(solution())