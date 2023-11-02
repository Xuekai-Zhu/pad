def solution():
    total_concrete_needed = 4800
    concrete_used_for_anchors = 700
    concrete_used_for_deck = 1600

    # Calculate the amount of concrete needed for the supporting pillars
    concrete_needed_for_pillars = total_concrete_needed - (concrete_used_for_deck + (2 * concrete_used_for_anchors))
    result = concrete_needed_for_pillars
    return result

print(solution())