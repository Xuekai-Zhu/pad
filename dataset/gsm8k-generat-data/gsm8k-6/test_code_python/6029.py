def solution():
    # Calculate the total amount of concrete needed for the anchors and the roadway deck
    total_concrete = 1600 + 700  # 1600 tons for the roadway deck and equal amounts for the two anchors, one of which has already been built using 700 tons

    # Calculate the amount of concrete needed for the supporting pillars
    pillar_concrete = 4800 - total_concrete  # total concrete in the entire bridge is 4800 tons, so the difference is the amount needed for the supporting pillars

    result = pillar_concrete
    return result

print(solution())