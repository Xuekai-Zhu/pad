def solution():
    # Total number of leaves fallen
    total_leaves = 7 + (4 * 2) # First hour: 7 leaves, Next 2 hours: 4 leaves per hour

    # Average number of leaves fallen per hour
    average_leaves = total_leaves / 3  # Total hours: 3

    result = average_leaves
    return result

print(solution())