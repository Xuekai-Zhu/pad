def solution():
    # Calculate the total number of leaves fallen
    total_leaves = 7 + (4 * 2)  # 7 leaves in first hour, and 4 leaves per hour in second and third hour

    # Calculate the average number of leaves fallen per hour
    avg_leaves = total_leaves / 3  # total hours = 3
    result = avg_leaves
    return result

print(solution())