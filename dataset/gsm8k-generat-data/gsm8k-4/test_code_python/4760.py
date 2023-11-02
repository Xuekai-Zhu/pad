def solution():
    """John weighs one-quarter times more than what Mary weighs. Mary weighs 20 lbs less than Jamison's weight. If Mary weighs 160 lbs, what's the combined weight of the three?"""
    # Calculate Jamison's weight
    jamison_weight = 160 + 20

    # Calculate Mary's weight
    mary_weight = 160

    # Calculate John's weight
    john_weight = 1.25 * mary_weight

    # Calculate the combined weight of the three
    total_weight = jamison_weight + mary_weight + john_weight

    result = total_weight
    return result

print(solution())