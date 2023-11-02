def solution():
    """At the family reunion, everyone ate too much food and gained weight. Orlando gained 5 pounds. Jose gained two pounds more than twice what Orlando gained. Fernando gained 3 pounds less than half of what Jose gained. How much weight, in pounds, did the three family members gain at their reunion?"""
    # Define the weight gained by Orlando
    Orlando_gain = 5

    # Define the weight gained by Jose
    Jose_gain = 2 + 2 * Orlando_gain

    # Define the weight gained by Fernando
    Fernando_gain = 0.5 * Jose_gain - 3

    # Calculate the total weight gained by the three family members
    total_gain = Orlando_gain + Jose_gain + Fernando_gain

    # Display the total weight gained
    result = total_gain
    return result

print(solution())