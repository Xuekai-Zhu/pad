def solution():
    # Calculate the total number of pizza slices Bobby has
    bobby_slices = 2 * 6  # Bobby has 2 pizzas and each pizza has 6 slices

    # Calculate the number of slices Mrs. Kaplan has, which is 1/4 of what Bobby has
    kaplan_slices = bobby_slices / 4

    result = kaplan_slices
    return result

print(solution())