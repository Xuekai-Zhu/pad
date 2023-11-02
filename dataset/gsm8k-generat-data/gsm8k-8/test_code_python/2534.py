def solution():
    # Calculate the total number of slices in both pies
    total_slices = 2 * 8

    # Subtract one slice from each pie for Rebecca's initial servings
    total_slices -= 2

    # Calculate the number of slices eaten by family and friends
    slices_eaten = 0.5 * total_slices

    # Subtract the slices eaten from the total slices
    total_slices -= slices_eaten

    # Subtract one slice each for Rebecca and her husband on Sunday evening
    total_slices -= 2

    result = total_slices
    return result

print(solution())