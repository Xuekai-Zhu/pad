def solution():
    """Karen hangs 6 ferns around her house. Each fern has 7 fronds, and each frond has 30 leaves. How many leaves do all the ferns have?"""
    # Define the number of ferns, fronds per fern, and leaves per frond
    FERNS = 6
    FRONDS_PER_FERN = 7
    LEAVES_PER_FROND = 30

    # Calculate the total number of fronds and leaves
    total_fronds = FERNS * FRONDS_PER_FERN
    total_leaves = total_fronds * LEAVES_PER_FROND

    # Display the total number of leaves
    result = total_leaves
    return result

print(solution())