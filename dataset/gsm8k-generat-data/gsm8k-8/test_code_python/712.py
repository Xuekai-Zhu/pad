def solution():
    # Calculate the total cost of pens
    pen_cost = 3 * 1

    # Calculate the total cost of notebooks
    notebook_cost = 4 * 3

    # Calculate the total cost of folders
    folder_cost = 2 * 5

    # Calculate the total cost of all items
    total_cost = pen_cost + notebook_cost + folder_cost

    # Calculate the change from the $50 bill
    change = 50 - total_cost
    result = change
    return result

print(solution())