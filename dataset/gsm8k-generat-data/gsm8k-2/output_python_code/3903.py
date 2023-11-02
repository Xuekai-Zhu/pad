def solution():
    """Mary needs school supplies. She has 6 classes and needs 1 folder for each class. She also needs 3 pencils for each class.
    She decides that for every 6 pencils she should have 1 eraser. She also needs a set of paints for an art class. Folders cost $6,
    pencils cost $2, and erasers cost $1. If she spends $80, how much did the set of paints cost in dollars?"""
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