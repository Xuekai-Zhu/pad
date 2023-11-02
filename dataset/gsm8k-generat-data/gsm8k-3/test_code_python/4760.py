def solution():
    """John weighs one-quarter times more than what Mary weighs. Mary weighs 20 lbs less than Jamison's weight. If Mary weighs 160 lbs, what's the combined weight of the three?"""
    # Calculate Jamison's weight
    jamison_weight = 160 + 20

    # Calculate John's weight
    john_weight = (5/4) * 160

    # Calculate the combined weight of the three
    combined_weight = john_weight + 160 + jamison_weight

    # Display the combined weight
    result = combined_weight
    return result

print(solution())