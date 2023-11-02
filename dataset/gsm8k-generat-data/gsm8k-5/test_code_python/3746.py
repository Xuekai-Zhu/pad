def solution():
    total_cost = 6  # The total cost of the pen and pencil is $6
    pen_cost = 0  # Let's initially set the cost of the pen to 0

    # We know that the pen costs twice as much as the pencil
    # Let's use the variable 'x' to represent the cost of the pencil
    # Then the cost of the pen will be 2*x
    # And the total cost will be x + 2*x = 3*x
    # So we can solve for x: x = total_cost / 3
    pencil_cost = total_cost / 3
    pen_cost = 2 * pencil_cost

    result = pen_cost
    return result

print(solution())