def solution():
    pencils_per_dozen = 12
    num_dozen_pencils = 2
    pencil_cost = 0.5

    num_folders = 20
    folder_cost = 0.9

    # Calculate the total cost of all pencils
    total_pencil_cost = num_dozen_pencils * pencils_per_dozen * pencil_cost

    # Calculate the total cost of all folders
    total_folder_cost = num_folders * folder_cost

    # Calculate the total cost of all office supplies
    total_cost = total_pencil_cost + total_folder_cost
    result = total_cost
    return result

print(solution())