def solution():
    total_passes = 50  # The quarterback throws 50 passes in total
    passes_right = 2 * passes_left  # He throws twice as many passes to the right as he does to the left
    passes_center = passes_left + 2  # He throws 2 more passes to the center than to the left

    # Set up an equation to solve for passes_left
    passes_left + passes_right + passes_center = total_passes

    # Simplify this equation using the values we already know
    passes_left + 2 * passes_left + (passes_left + 2) = 50
    4 * passes_left + 2 = 50

    # Solve for passes_left
    passes_left = (50 - 2) / 4
    result = passes_left
    return result

print(solution())