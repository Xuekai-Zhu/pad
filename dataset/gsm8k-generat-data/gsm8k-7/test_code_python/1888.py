def solution():
    num_streetlights_bought = 200
    num_squares = 15
    num_streetlights_per_square = 12

    # Calculate the total number of streetlights that will be used
    total_streetlights_needed = num_squares * num_streetlights_per_square

    # Calculate the number of unused streetlights
    num_unused_streetlights = num_streetlights_bought - total_streetlights_needed
    result = num_unused_streetlights
    return result

print(solution())