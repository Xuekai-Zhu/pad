def solution():
    ferns = 6  # Karen has 6 ferns
    fronds_per_fern = 7  # Each fern has 7 fronds
    leaves_per_frond = 30  # Each frond has 30 leaves

    # Calculate the total number of leaves for all the ferns
    total_leaves = ferns * fronds_per_fern * leaves_per_frond
    result = total_leaves
    return result

print(solution())