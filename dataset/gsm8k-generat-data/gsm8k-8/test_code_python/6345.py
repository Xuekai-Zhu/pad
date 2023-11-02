def solution():
    # Define the number of ferns, fronds, and leaves per frond
    num_ferns = 6
    fronds_per_fern = 7
    leaves_per_frond = 30

    # Calculate the total number of leaves
    total_leaves = num_ferns * fronds_per_fern * leaves_per_frond
    result = total_leaves
    return result

print(solution())