def solution():
    num_classes = 6  # Mary has 6 classes
    num_folders = num_classes  # Mary needs 1 folder for each class
    num_pencils = 3 * num_classes  # Mary needs 3 pencils for each class
    num_erasers = num_pencils // 6  # Mary needs 1 eraser for every 6 pencils

    # Calculate the cost of folders, pencils, and erasers
    cost_folders = num_folders * 6  # Folders cost $6 each
    cost_pencils = num_pencils * 2  # Pencils cost $2 each
    cost_erasers = num_erasers * 1  # Erasers cost $1 each

    # Calculate the total cost of school supplies
    total_cost = cost_folders + cost_pencils + cost_erasers

    # Calculate the cost of the paints
    cost_paints = 80 - total_cost
    result = cost_paints
    return result

print(solution())