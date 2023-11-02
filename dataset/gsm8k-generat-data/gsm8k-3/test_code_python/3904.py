def solution():
    """Mary needs school supplies. She has 6 classes and needs 1 folder for each class. 
    She also needs 3 pencils for each class. She decides that for every 6 pencils she should have 1 eraser.
    She also needs a set of paints for an art class. Folders cost $6, pencils cost $2, and erasers cost $1. 
    If she spends $80, how much did the set of paints cost in dollars?"""
    num_classes = 6
    num_folders = num_classes
    num_pencils = num_classes * 3
    num_erasers = num_pencils // 6
    num_paints = 1
    folder_cost = 6
    pencil_cost = 2
    eraser_cost = 1
    paint_cost = (80 - (num_folders * folder_cost + num_pencils * pencil_cost + num_erasers * eraser_cost)) / num_paints
    result = paint_cost
    return result

print(solution())