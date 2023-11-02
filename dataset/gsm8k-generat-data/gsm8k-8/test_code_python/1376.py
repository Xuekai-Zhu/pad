def solution():
    # Define total number of leaves collected
    total_leaves = 12 + 13

    # Calculate the number of brown and green leaves
    brown_green_leaves = int(0.2 * total_leaves)

    # Calculate the number of yellow leaves
    yellow_leaves = total_leaves - brown_green_leaves

    # Return the result
    result = yellow_leaves
    return result

print(solution())