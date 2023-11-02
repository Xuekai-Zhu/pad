def solution():
    """Tyler weighs 25 pounds more than Sam. Peter weighs half as much as Tyler. If Peter weighs 65 pounds, how much does Sam weigh, in pounds?"""
    # Define Peter's weight and Tyler-Sam weight difference
    PETER_WEIGHT = 65
    TYLER_SAM_DIFFERENCE = 25

    # Calculate Tyler's weight
    tyler_weight = PETER_WEIGHT * 2

    # Calculate Sam's weight
    sam_weight = tyler_weight - TYLER_SAM_DIFFERENCE

    # Display Sam's weight
    result = sam_weight
    return result

print(solution())