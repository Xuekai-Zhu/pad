def solution():
    # Calculate the total cost of the folders and pencils
    num_classes = 6
    folder_cost = 6 * num_classes
    pencil_cost = 2 * 3 * num_classes
    eraser_cost = 1 * (pencil_cost // 6)  # Use integer division to find number of erasers needed
    total_cost = folder_cost + pencil_cost + eraser_cost

    # Calculate the cost of the set of paints
    paint_cost = 80 - total_cost
    result = paint_cost
    return result

print(solution())