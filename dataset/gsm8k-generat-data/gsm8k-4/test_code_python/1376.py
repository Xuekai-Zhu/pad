def solution():
    """Bronson decides to collect Oak Leaves from around his Neighborhood. He collects 12 on Thursday and 13 on Friday. 20% are Brown and 20% are Green. The rest are yellow. How many yellow leaves does he collect?"""
    # Define the total number of leaves collected
    total_leaves = 12 + 13

    # Calculate the number of brown leaves
    brown_leaves = total_leaves * 0.2

    # Calculate the number of green leaves
    green_leaves = total_leaves * 0.2

    # Calculate the number of yellow leaves
    yellow_leaves = total_leaves - brown_leaves - green_leaves

    result = yellow_leaves
    return result

print(solution())