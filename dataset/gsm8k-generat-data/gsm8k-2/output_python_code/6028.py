def solution():
    """Johnny is an engineer designing a bridge. The roadway deck for the top of the bridge needs 1600 tons of concrete to construct. The two bridge anchors need equal amounts of concrete, but only one has been built so far, using 700 tons of concrete. Johnny had to calculate how many tons of concrete the supporting pillars underneath the bridge would need, and he found that the total amount of concrete in the entire bridge will be 4800 tons. How much concrete did Johnny find he needs for the supporting pillars?"""
    roadway_deck = 1600
    bridge_anchors = 700
    total_concrete = 4800
    supporting_pillars = total_concrete - roadway_deck - (2 * bridge_anchors)
    result = supporting_pillars
    return result

print(solution())