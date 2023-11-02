def solution():
    """Johnny is an engineer designing a bridge. The roadway deck for the top of the bridge needs 1600 tons of concrete to construct. The two bridge anchors need equal amounts of concrete, but only one has been built so far, using 700 tons of concrete. Johnny had to calculate how many tons of concrete the supporting pillars underneath the bridge would need, and he found that the total amount of concrete in the entire bridge will be 4800 tons. How much concrete did Johnny find he needs for the supporting pillars?"""
    # Define the total amount of concrete in the entire bridge
    total_concrete = 4800

    # Define the amount of concrete used for the roadway deck and one bridge anchor
    deck_and_anchor_concrete = 1600 + 700

    # Calculate the amount of concrete needed for the supporting pillars
    pillars_concrete = total_concrete - deck_and_anchor_concrete

    # return the result
    result = pillars_concrete
    return result

print(solution())