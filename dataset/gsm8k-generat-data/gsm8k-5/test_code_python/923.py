def solution():
    length = 7  # The quilt has a length of 7 feet
    width = 8  # The quilt has a width of 8 feet
    cost_per_square_foot = 40  # The quilt costs $40 per square foot

    # Calculate the total area of the quilt in square feet
    total_area = length * width

    # Calculate the total cost of the quilt
    total_cost = total_area * cost_per_square_foot
    result = total_cost
    return result

print(solution())