def solution():
    eraser_cost = 2
    pencil_cost = 3
    num_erasers = 6
    num_pencils = 8

    # Calculate the total cost of erasers
    eraser_total_cost = eraser_cost * num_erasers

    # Calculate the total cost of pencils
    pencil_total_cost = pencil_cost * num_pencils

    # Calculate the total cost of all items
    total_cost = eraser_total_cost + pencil_total_cost
    result = total_cost
    return result

print(solution())