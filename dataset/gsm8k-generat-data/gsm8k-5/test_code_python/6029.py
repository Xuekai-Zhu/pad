def solution():
    # Calculate the total amount of concrete needed for the two bridge anchors
    total_concrete_anchors = 1600 - 700  # The first anchor has been built using 700 tons of concrete
    # Divide the remaining amount equally between the two anchors
    concrete_per_anchor = total_concrete_anchors / 2  

    # Calculate the amount of concrete needed for the supporting pillars
    concrete_supporting_pillars = 4800 - 1600 - total_concrete_anchors

    result = concrete_supporting_pillars
    return result

print(solution())