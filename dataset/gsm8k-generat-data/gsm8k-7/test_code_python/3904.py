def solution():
    num_classes = 6
    num_folders = num_classes
    num_pencils_per_class = 3
    num_erasers_per_6_pencils = 1
    num_paint_sets = 1

    folder_cost = 6
    pencil_cost = 2
    eraser_cost = 1

    total_cost = num_folders * folder_cost +\
                 num_classes * num_pencils_per_class * pencil_cost +\
                 (num_classes // 6) * num_erasers_per_6_pencils * eraser_cost +\
                 num_paint_sets * ???  # we need to find the cost of the paint set

    # We know that the total cost is $80, so we can algebraically solve for the paint set cost
    paint_set_cost = (80 - total_cost) / num_paint_sets

    result = paint_set_cost
    return result

print(solution())