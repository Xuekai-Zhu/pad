def solution():
    # Define the cost of a pencil and a folder
    pencil_cost = 0.5
    folder_cost = 0.9

    # Calculate the total cost of pencils and folders
    total_pencil_cost = 2 * 12 * pencil_cost
    total_folder_cost = 20 * folder_cost

    # Calculate the total cost of office supplies
    total_cost = total_pencil_cost + total_folder_cost
    result = total_cost
    return result

print(solution())