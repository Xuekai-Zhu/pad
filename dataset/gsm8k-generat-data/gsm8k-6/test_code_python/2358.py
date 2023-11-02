def solution():
    # Calculate the total cost of pencils and folders
    dozen = 12
    num_pencils = 2 * dozen
    num_folders = 20
    cost_pencils = 0.5 * num_pencils
    cost_folders = 0.9 * num_folders
    total_cost = cost_pencils + cost_folders
    result = total_cost
    return result

print(solution())