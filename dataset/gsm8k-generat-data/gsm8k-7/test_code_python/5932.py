def solution():
    sharpening_per_pencil = 5
    sharpening_per_hour = 1 / 1.5
    num_available_pencils = 10
    num_needed_hours = 105
    pencil_cost = 2

    # Calculate the total number of sharpenings that Jenine needs
    num_needed_sharpenings = num_needed_hours / sharpening_per_hour

    # Calculate the total number of pencils that Jenine needs
    num_needed_pencils = num_needed_sharpenings / sharpening_per_pencil

    # Calculate the number of additional pencils that Jenine needs to buy
    num_additional_pencils = num_needed_pencils - num_available_pencils

    # Calculate the cost of the additional pencils
    cost_additional_pencils = num_additional_pencils * pencil_cost
    result = cost_additional_pencils
    return result

print(solution())