def solution():
    """Johnny is an engineer designing a bridge. The roadway deck for the top of the bridge needs 1600 tons of concrete to construct. The two bridge anchors need equal amounts of concrete, but only one has been built so far, using 700 tons of concrete. Johnny had to calculate how many tons of concrete the supporting pillars underneath the bridge would need, and he found that the total amount of concrete in the entire bridge will be 4800 tons. How much concrete did Johnny find he needs for the supporting pillars?"""
    # Define the total amount of concrete needed for the bridge and the anchor already built
    total_concrete = 4800
    anchor_concrete = 700

    # Calculate the amount of concrete needed for the other anchor
    anchor_total = total_concrete - anchor_concrete
    anchor_per_side = anchor_total / 2

    # Calculate the amount of concrete needed for the roadway deck and subtract it from the total
    roadway_concrete = 1600
    remaining_concrete = total_concrete - roadway_concrete - anchor_total

    # Display the amount of concrete needed for the supporting pillars
    result = remaining_concrete
    return result

print(solution())