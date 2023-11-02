def solution():
    # Set up equations based on the given information
    ron_weight = x
    roger_weight = 4*x - 7
    rodney_weight = 2*(4*x - 7)

    # Find the total weight they can lift together
    total_weight = ron_weight + roger_weight + rodney_weight

    # Solve for x (Ron's weight)
    x = (239 - 2*(4*x - 7)) / 5

    # Calculate Rodney's weight (twice Roger's weight)
    rodney_weight = 2 * (4*x - 7)

    result = rodney_weight
    return result

print(solution())