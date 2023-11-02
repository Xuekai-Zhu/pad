def solution():
    
    roadway_deck = 1600
    bridge_anchors = 700
    total_concrete = 4800
    supporting_pillars = total_concrete - roadway_deck - (2 * bridge_anchors)
    result = supporting_pillars
    return result

print(solution())