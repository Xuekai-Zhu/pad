def solution():
    """At the family reunion, everyone ate too much food and gained weight. Orlando gained 5 pounds. Jose gained two pounds more than twice what Orlando gained. Fernando gained 3 pounds less than half of what Jose gained. How much weight, in pounds, did the three family members gain at their reunion?"""
    # Define the weight gained by Orlando
    orlando_weight = 5

    # Define the weight gained by Jose
    jose_weight = 2 + 2 * orlando_weight

    # Define the weight gained by Fernando
    fernando_weight = (jose_weight / 2) - 3

    # Calculate the total weight gained by the three family members
    total_weight = orlando_weight + jose_weight + fernando_weight

    result = total_weight
    return result

print(solution())