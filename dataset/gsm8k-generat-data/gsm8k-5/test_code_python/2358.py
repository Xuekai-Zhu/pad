def solution():
    pencils_per_dozen = 12  # There are 12 pencils in a dozen
    folders_per_unit = 1  # Office needs 20 folders

    # Calculate the total cost of pencils
    total_pencil_cost = 0.5 * pencils_per_dozen * 2  # Two dozens of pencils needed

    # Calculate the total cost of folders
    total_folder_cost = 0.9 * folders_per_unit * 20  # 20 folders needed

    # Calculate the total cost of all office supplies
    total_cost = total_pencil_cost + total_folder_cost
    result = total_cost
    return result

print(solution())