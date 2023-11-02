def solution():
    num_ferns = 6
    fronds_per_fern = 7
    leaves_per_frond = 30

    # Calculate the total number of fronds
    total_fronds = num_ferns * fronds_per_fern

    # Calculate the total number of leaves
    total_leaves = total_fronds * leaves_per_frond
    result = total_leaves
    return result

print(solution())