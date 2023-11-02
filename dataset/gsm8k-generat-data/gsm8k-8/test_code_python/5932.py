def solution():
    # Calculate the total number of pencils needed
    total_hours = 105
    sharpen_interval = 1.5
    sharpen_per_pencil = 5
    total_sharpens = total_hours / sharpen_interval
    total_pencils = total_sharpens / sharpen_per_pencil
    existing_pencils = 10
    pencils_needed = total_pencils - existing_pencils

    # Calculate the cost of the additional pencils
    pencil_cost = 2
    total_cost = pencils_needed * pencil_cost
    result = total_cost
    return result

print(solution())