def solution():
    """Tyler weighs 25 pounds more than Sam. Peter weighs half as much as Tyler. If Peter weighs 65 pounds, how much does Sam weigh, in pounds?"""
    # Define Peter's weight
    peter_weight = 65

    # Calculate Tyler's weight
    tyler_weight = peter_weight * 2

    # Calculate Sam's weight
    sam_weight = tyler_weight - 25

    # Return Sam's weight
    result = sam_weight
    return result

print(solution())