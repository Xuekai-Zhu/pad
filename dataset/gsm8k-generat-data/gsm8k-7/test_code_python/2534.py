def solution():
    num_pies = 2
    slices_per_pie = 8
    num_slices_eaten = 2

    # Calculate the total number of slices of pie
    total_slices = num_pies * slices_per_pie

    # Subtract the slices that Rebecca and her husband ate
    remaining_slices = total_slices - num_slices_eaten

    # Calculate the number of slices eaten by family and friends
    eaten_slices = remaining_slices * 0.5

    # Subtract the slices eaten by family and friends
    remaining_slices -= eaten_slices

    # Rebecca and her husband each have another slice of pie
    remaining_slices -= 2

    result = remaining_slices
    return result

print(solution())