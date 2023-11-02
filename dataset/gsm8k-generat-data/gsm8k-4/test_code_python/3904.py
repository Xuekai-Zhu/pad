def solution():
    """Mary needs school supplies. She has 6 classes and needs 1 folder for each class. She also needs 3 pencils for each class. She decides that for every 6 pencils she should have 1 eraser. She also needs a set of paints for an art class. Folders cost $6, pencils cost $2, and erasers cost $1. If she spends $80, how much did the set of paints cost in dollars?"""
    # Define the number of classes and the number of pencils needed per class
    num_classes = 6
    pencils_per_class = 3

    # Calculate the total number of pencils needed
    total_pencils = num_classes * pencils_per_class

    # Calculate the number of erasers needed based on the number of pencils
    num_erasers = total_pencils // 6

    # Calculate the cost of the folders, pencils, and erasers
    folder_cost = num_classes * 6
    pencil_cost = total_pencils * 2
    eraser_cost = num_erasers * 1

    # Calculate the remaining budget for the set of paints
    paint_cost = 80 - folder_cost - pencil_cost - eraser_cost

    # return the result
    result = paint_cost
    return result

print(solution())