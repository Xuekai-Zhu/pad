def solution():
    # Calculation of Hawaiian pizza slices
    hawaiian_slices = 12 * 2 / 2  # Half of one pizza

    # Calculation of cheese pizza slices
    cheese_slices = 12 * 2

    # Calculation of slices that Frank ate
    frank_slices = 3

    # Calculation of slices that Sammy ate
    sammy_slices = cheese_slices / 3

    # Calculation of total slices eaten
    total_slices_eaten = hawaiian_slices + frank_slices + sammy_slices

    # Calculation of total slices left over
    total_slices_left = (12 * 2) - total_slices_eaten  # total number of slices - slices eaten

    result = total_slices_left
    return result

print(solution())