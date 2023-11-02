def solution():
    # Calculate the length of the three sides that need fencing
    side1 = 9
    side2 = 9
    side3 = 18
    total_length = side1 + side2 + side3

    # Calculate the cost of fencing the shared sides with the two neighbors
    shared_side1_cost = (1/2) * 9 * 3 # the neighbor behind pays for half of a 9-foot shared side
    shared_side2_cost = (1/3) * 9 * 3 # the neighbor on the left pays for a third of a 9-foot shared side
    shared_sides_cost = shared_side1_cost + shared_side2_cost

    # Calculate the total cost of fencing
    total_cost = (total_length * 3) - shared_sides_cost  # $3 per foot

    result = total_cost
    return result

print(solution())