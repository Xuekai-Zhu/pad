def solution():
    """At the family reunion, everyone ate too much food and gained weight. Orlando gained 5 pounds. Jose gained two pounds more than twice what Orlando gained. Fernando gained 3 pounds less than half of what Jose gained. How much weight, in pounds, did the three family members gain at their reunion?"""
    orlando_gain = 5
    jose_gain = 2 + 2 * orlando_gain
    fernando_gain = (jose_gain / 2) - 3
    total_gain = orlando_gain + jose_gain + fernando_gain
    result = total_gain
    return result

print(solution())