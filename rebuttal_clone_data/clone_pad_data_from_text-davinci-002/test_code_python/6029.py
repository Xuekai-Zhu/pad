def solution():
    total_concrete = 4800
    deck_concrete = 1600
    anchors_concrete = total_concrete - deck_concrete
    pillars_concrete = anchors_concrete / 2
    result = pillars_concrete
    return result

print(solution())