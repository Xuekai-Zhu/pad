def solution():
    """Bill's roof can bear 500 pounds of weight. If 100 leaves fall on his roof every day, and 1000 leaves weighs 1 pound, how many days will it take for his roof to collapse?"""
    # Define the weight of one leaf and the maximum weight the roof can bear
    leaf_weight = 0.001
    max_weight = 500

    # Calculate the total weight of leaves that can accumulate on the roof before it collapses
    max_leaves = max_weight / leaf_weight * 1000

    # Calculate the number of days before the roof collapses
    days = max_leaves / 100

    # Return the result rounded up to the nearest integer
    result = math.ceil(days)
    return result

print(solution())