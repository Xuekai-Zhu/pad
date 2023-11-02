def solution():
    """Karen hangs 6 ferns around her house. Each fern has 7 fronds, and each frond has 30 leaves. How many leaves do all the ferns have?"""
    ferns = 6
    fronds_per_fern = 7
    leaves_per_frond = 30
    total_leaves = ferns * fronds_per_fern * leaves_per_frond
    result = total_leaves
    return result

print(solution())