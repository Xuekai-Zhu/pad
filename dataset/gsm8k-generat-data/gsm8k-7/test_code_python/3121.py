def solution():
    total_slices = 8
    angeli_slices = 3/2
    marlon_slices = 3/2

    # Calculate the total slices eaten by Angeli and Marlon
    total_slices_eaten = angeli_slices + marlon_slices

    # Calculate the remaining slices of pizza
    remaining_slices = total_slices - total_slices_eaten
    result = remaining_slices
    return result

print(solution())